// CAN Receive for GFunkbus76's custom Can Bus VW Bus
// Using MCP2515 module connected to an Arduino Nano
// Receives from Arduino Mega
// Outputs data to Raspberry Pi 4 4gb via Serial USB connection
// 2020
// This is a conglomeration of various example code and snippets from the internet
// *** USE AT YOUR OWN RISK ***
//

#include <mcp_can.h>
#include <SPI.h>

long unsigned int rxId;
unsigned char len = 0;
unsigned char rxBuf[8];
char msgString[128];                        // Array to store serial string

// ITEMS TO OUTPUT VIA CAN ... VARIABLES

unsigned int engine_rpm;
unsigned int speed_cv;
unsigned int coolant;
float boost;
unsigned int egt;
float oil_pressure;
unsigned int fuel;
unsigned int outside_temp;
unsigned char temp;

#define CAN0_INT 2                              // Set INT to pin 2
MCP_CAN CAN0(10);                               // Set CS to pin 10


void setup()
{
  Serial.begin(115200);

  // Initialize MCP2515 running at 8MHz with a baudrate of 500kb/s and the masks and filters disabled.
  if (CAN0.begin(MCP_ANY, CAN_500KBPS, MCP_8MHZ) == CAN_OK)
    Serial.println("MCP2515 Initialized Successfully!");
  else
    Serial.println("Error Initializing MCP2515...");

  CAN0.setMode(MCP_NORMAL);                     // Set operation mode to normal so the MCP2515 sends acks to received data.

  pinMode(CAN0_INT, INPUT);                            // Configuring pin for /INT input

  Serial.println("Receiving CAN BUS Messages ...");
}

void loop()
{
  if (!digitalRead(CAN0_INT))                        // If CAN0_INT pin is low, read receive buffer
  {
    CAN0.readMsgBuf(&rxId, &len, rxBuf);      // Read data: len = data length, buf = data byte(s)

    //    if ((rxId & 0x80000000) == 0x80000000)    // Determine if ID is standard (11 bits) or extended (29 bits)
    //      sprintf(msgString, "Extended ID: 0x%.8lX  DLC: %1d  Data:", (rxId & 0x1FFFFFFF), len);
    //    else
    sprintf(msgString, "Standard ID: 0x%.3lX    DLC: %1d  Data:", rxId, len);

    //Serial.print(msgString);

    if ((rxId) == 0x036) {  // Determine if message is a remote request frame.

      //    EGT Gauge (two bytes, combined)
      egt = rxBuf[0];
      egt = egt << 8;
      temp = rxBuf[1];
      egt = egt + temp;
      Serial.print("EGT: ");
      Serial.println(egt);

      
      //    Oil Pressure Values /100 due to scaling on transmission
      oil_pressure = rxBuf[2];
      oil_pressure = oil_pressure / 100;
      Serial.print("OIL PRESSURE: ");
      Serial.println(oil_pressure);

      //    Boost value / 100 due to scaling
      boost = rxBuf[3];
      boost = boost / 100;
      Serial.print("BOOST: ");
      Serial.println(boost);

      //    Coolant Temp Value
      coolant = rxBuf[4];
      Serial.print("COOLANT: ");
      Serial.println(coolant);

      //    RPM Values
      engine_rpm = rxBuf[5];
      engine_rpm = engine_rpm << 8;
      temp = rxBuf[6];
      engine_rpm = engine_rpm + temp;
      Serial.print("RPM:");
      Serial.println(engine_rpm);

      //    Fuel Sending Levels
      fuel = rxBuf[7];
      Serial.print("FUEL:");
      Serial.println(fuel);
      Serial.println();

    }
  }
}


//  }
//}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
