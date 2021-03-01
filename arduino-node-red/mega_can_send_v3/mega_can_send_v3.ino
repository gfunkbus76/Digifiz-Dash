
// GFunkbus76 - Arduino Engine Bay Monitoring System - Oct 2020
// Currently managing the following via sensor data
//  EGT Sensor - https://www.amazon.ca/gp/product/B00OZTNFCW/
//  Oil Pressure - 150psi 3-wire Pressure Transducer
//  Boost Pressure - 100psi 3-wire Pressure Transducer
//


#include <SPI.h>
#include <max6675.h> // egt
#include <mcp2515.h> // canbus
#include <Wire.h> // for pressure transducers (Boost/Oil Pressure)

// EGT Sensor
int thermoDO = 4;
int thermoCS = 5;
int thermoCLK = 6;
MAX6675 thermocouple(thermoCLK, thermoCS, thermoDO);
int vccPin = 3;
int gndPin = 2;

// Boost Sensor - pulled from https://www.youtube.com/watch?v=UrqPxwsPWGk&t=679s - Tyler at tylerovens@me.com
const int boostInput = A0; //select the analog input pin for the pressure transducer
const int pressureZero = 102.4; //analog reading of pressure transducer at 0psi
const int pressureMax = 921.6; //analog reading of pressure transducer at 100psi
const int boostmaxPSI = 100; //psi value of transducer being used
//const int baudRate = 9600; //constant integer to set the baud rate for serial monitor
const int sensorreadDelay = 250; //constant integer to set the sensor read delay in milliseconds

float boostValue = 0; //variable to store the value coming from the pressure transducer


// Voltage Sensor Module
int voltInput = A1;
float vout = 0.0;
float vin = 0.0;
float R1 = 30000.0; //  
float R2 = 7500.0; // 
int value = 0;


//Setting of the canbus messages we're sending
struct can_frame canMsg; //egt
struct can_frame canMsg1; //rpm
struct can_frame canMsg2; //?
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

  // Voltage Sensor Details
  pinMode(voltInput, INPUT);

  Serial.println("CANBUS Engine Control Module Test");
  //   wait for MAX chip to stabilize
  delay(500);
}

void loop() {
  // EGT Stuff
  //int egt = thermocouple.readFahrenheit(); //get egt temp
  int32_t egtDataF = (thermocouple.readFahrenheit());
  int32_t egtDataC = (thermocouple.readCelsius());
  //  int32_t egtDataC = (thermocouple.readCelsius());

  // Boost Sensor - pulled from https://www.youtube.com/watch?v=UrqPxwsPWGk&t=679s - Tyler at tylerovens@me.com
  boostValue = analogRead(boostInput); //reads value from input pin and assigns to variable
  boostValue = ((boostValue-pressureZero)*boostmaxPSI)/(pressureMax-pressureZero); //conversion equation to convert analog reading to psi
  int32_t boostData = boostValue * 100; // times 100 to increase to 2 decimal places - divided by 100 on receive end

  
  // Voltage Sensor
  value = analogRead(voltInput);
  vout = (value * 5.0) / 1024.0; // see text
  vin = vout / (R2/(R1+R2));
  int32_t voltage = vin * 100; // times 100 to increase to 2 decimal places - divided by 100 on receive end
 // int32_t voltage = (vin);


  // int egt = thermocouple.readCelsius(); //get egt temp
  // egt=map(egt,0,1023,0,255);
  // newegt = (egt[0] <<8) + egt[1];

  canMsg.can_id  = 0x036;           //CAN id as 0x036
  canMsg.can_dlc = 8;               //CAN data length as 8
  canMsg.data[0] = egtDataC;             //Update egt value in [0]
  canMsg.data[1] = egtDataC >> 8;            //Rest all with 0
  canMsg.data[2] = egtDataC >> 16;
  canMsg.data[3] = boostData;             //Update egt value in [0]
  canMsg.data[4] = voltage;           //Rest all with 0
  canMsg.data[5] = voltage >> 8;
  canMsg.data[6] = 0x00;
  canMsg.data[7] = 0x00;
  mcp2515.sendMessage(&canMsg);     //Sends the CAN message

 /* canMsg.can_id  = 0x037;           //CAN id as 0x036
  canMsg1.can_dlc = 8;               //CAN data length as 8
  canMsg1.data[0] = egtDataF;             //Update egt value in [0]
  canMsg1.data[1] = egtDataF >> 8;            //Rest all with 0
  canMsg1.data[2] = egtDataF >> 16;
  canMsg1.data[3] = egtDataC;             //Update egt value in [0]
  canMsg1.data[4] = egtDataC >> 8;            //Rest all with 0
  canMsg1.data[5] = egtDataC >> 16;
  canMsg1.data[6] = 0x00;
  canMsg1.data[7] = 0x00;
  mcp2515.sendMessage(&canMsg);     //Sends the CAN message
*/
  Serial.println(egtDataC, 1); //EGTC
  Serial.println(egtDataF); //EGTF
  Serial.println(boostValue, 1); // Boost one decimal place
  Serial.println(vin, 2); // Voltage

  delay(500);

  delay(50);
}
