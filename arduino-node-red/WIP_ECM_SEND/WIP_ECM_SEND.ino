/*
// GFunkbus76 - Arduino Engine Bay Monitoring System - March 2021
// Currently managing the following via sensor data
//  EGT Sensor - https://www.amazon.ca/gp/product/B00OZTNFCW/
//  Oil Pressure - 150psi 3-wire Pressure Transducer
//  Boost Pressure - 100psi 3-wire Pressure Transducer
//
//  Working on adding: Coolant / RPM / Fuel - as well as some dummy lights
//
*/

#include <SPI.h>
#include <max6675.h>    // For EGT Sensor
#include <can.h>        // Cory j Fowler Canbus Libray
#include <mcp2515.h>    // Cory j Fowler Canbus Libray
#include <Wire.h>       // for pressure transducers (Boost/Oil Pressure)

// EGT
//      From an library example
int thermoDO = 4;
int thermoCS = 5;
int thermoCLK = 6;
MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);
int vccPin = 3;
int gndPin = 2;

// BOOST
//      pulled from https://www.youtube.com/watch?v=UrqPxwsPWGk&t=679s - Tyler at tylerovens@me.com
const int boostInput = A0; //select the analog input pin for the pressure transducer
const int pressureZero = 102.4; //analog reading of pressure transducer at 0psi
const int pressureMax = 921.6; //analog reading of pressure transducer at 100psi
const int boostmaxPSI = 100; //psi value of transducer being used
//const int baudRate = 9600; //constant integer to set the baud rate for serial monitor
const int sensorreadDelay = 250; //constant integer to set the sensor read delay in milliseconds
float boostValue = 0; //variable to store the value coming from the pressure transducer

// OIL PRESSURE
//      pulled from https://www.youtube.com/watch?v=UrqPxwsPWGk&t=679s - Tyler at tylerovens@me.com
const int oilpressureInput = A1; //select the analog input pin for the pressure transducer
const int oilpressuremaxPSI = 150; //psi value of transducer being used
float oilpressureValue = 0; //variable to store the value coming from the pressure transducer

//  SETTING CAN BUS MESSAGE QTY
//        basic details of the can signals we are sending from the Engine Bay
struct can_frame canMsg;    //    Sensor Data: EGT,  OIL PRESSURE, BOOST,  COOLANT,  RPM,  FUEL   
struct can_frame canMsg1;   //    Dummy Lights and more: Oil Light(pin drops low?), ALT Light?, Reverse Indicator
MCP2515 mcp2515(53); // Pin



void setup()
{
  while (!Serial);
  Serial.begin(115200);
  SPI.begin();

  // EGT Pin Details
  pinMode(vccPin, OUTPUT); digitalWrite(vccPin, HIGH);
  pinMode(gndPin, OUTPUT); digitalWrite(gndPin, LOW);

  // CANBUS Board details
  mcp2515.reset();
  mcp2515.setBitrate(CAN_500KBPS, MCP_8MHZ); //Sets CAN at speed 500KBPS and Clock 8MHz
  mcp2515.setNormalMode();
  
  Serial.println("CANBUS Engine Control Module Test");
  //   wait for MAX chip to stabilize
  delay(500);
}

void loop() {
  // EGT Stuff
  int32_t egtDataC = (thermocouple.readCelsius());
  uint8_t lowbyte = egtDataC & 0xFF;
  uint8_t highbyte = egtDataC >> 8;
  
  // Boost Sensor - pulled from https://www.youtube.com/watch?v=UrqPxwsPWGk&t=679s - Tyler at tylerovens@me.com
  boostValue = analogRead(boostInput); //reads value from input pin and assigns to variable
  boostValue = ((boostValue - pressureZero) * boostmaxPSI) / (pressureMax - pressureZero); //conversion equation to convert analog reading to psi
  int32_t boostData = boostValue * 100; // times 100 to increase to 2 decimal places - divided by 100 on receive end


  // Oil Pressure Sensor - pulled from https://www.youtube.com/watch?v=UrqPxwsPWGk&t=679s - Tyler at tylerovens@me.com
  oilpressureValue = analogRead(oilpressureInput); //reads value from input pin and assigns to variable
  oilpressureValue = ((oilpressureValue - pressureZero) * oilpressuremaxPSI) / (pressureMax - pressureZero); //conversion equation to convert analog reading to psi
  int32_t oilpressureData = oilpressureValue * 100; // times 100 to increase to 2 decimal places - divided by 100 on receive end

  //    Preparing the CAN BUS Messages
  canMsg.can_id  = 0x036;           //CAN id as 0x036
  canMsg.can_dlc = 8;               //CAN data length as 8
  canMsg.data[0] = highbyte;        //Update egt value in [0]
  canMsg.data[1] = lowbyte;         // EGT second value
  canMsg.data[2] = oilpressureData;     //Oilpressure - psi
  canMsg.data[3] = boostData;         //  Update boost - psi
  canMsg.data[4] = 0x00;              //  Coolant - *C
  canMsg.data[5] = 0x00;              //  RPM 1
  canMsg.data[6] = 0x00;              //  RPM 2
  canMsg.data[7] = 0x00;              //  Fuel - 0-255?
  mcp2515.sendMessage(&canMsg);     //Sends the CAN message
  
  //    Second CAN BUS Message
  canMsg1.can_id  = 0x037;           //CAN id as 0x037
  canMsg1.can_dlc = 8;               //CAN data length as 8
  canMsg1.data[0] = 0x00;             
  canMsg1.data[1] = 0x10;            
  canMsg1.data[2] = 0x00;
  canMsg1.data[3] = 0x10;             
  canMsg1.data[4] = 0x00;            
  canMsg1.data[5] = 0x10;
  canMsg1.data[6] = 0x10;
  canMsg1.data[7] = 0x00;
  mcp2515.sendMessage(&canMsg1);     //Sends the CAN message

  Serial.print("EGT: ");
  Serial.println(egtDataC); //EGTF
  Serial.print("BOOST: ");
  Serial.println(boostValue, 1); // Boost one decimal place
  Serial.print("OILPRESSURE: ");
  Serial.println(oilpressureValue, 1); // Voltage

  delay(500);

  delay(50);
}
