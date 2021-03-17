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

    sprintf(msgString, "Standard ID: 0x%.3lX    DLC: %1d  Data:", rxId, len);

    //Serial.print(msgString);

    if ((rxId & 0x40000000) == 0x40000000) {  // Determine if message is a remote request frame.
      sprintf(msgString, " REMOTE REQUEST FRAME");
      // Serial.print(msgString);
    } else {
      //        for(byte i = 0; i<len; i++){
      //         sprintf(msgString, " 0x%.2X", rxBuf[i]);
      //       Serial.print(msgString);


      if (rxId & 0x0360 == 0x0360) {

        unsigned int receivedEGTc = 0;
        receivedEGTc = rxBuf[0] <<8 | rxBuf[1];
        
        int32_t oilP = rxBuf[2];
        int32_t boost = rxBuf[3];
        //int32_t voltage = rxBuf[5];

        //egtc = (egtc << 8) | rxBuf[1];
        //egtc = (egtc << 8) | rxBuf[0];

        oilP = rxBuf[2];
        float oilPData = oilP;
        float oilPDisplay = oilPData / 10;
      
        
        boost = rxBuf[3];
        float boostData = boost;
        float boostDisplay = boostData / 10;

        //voltage = (voltage << 8) | rxBuf[4];
        // Convert voltage to float and then divide by sending multiplier (100) to display accurate decimal version
        //float vin = voltage;
        //float volt = vin / 100;
        //      char volt[8];
        //    dtostrf(vin, 6, 2, volt);
        //  Serial.print("EGT(c): ");
        Serial.print(receivedEGTc);
        Serial.print(",");
        //      Serial.print("Boost(bar): ");
        Serial.print(boostDisplay);
        Serial.print(",");
        //      Serial.print("Voltage: ");
        Serial.print(oilPDisplay);
        Serial.print("");

      }
      Serial.println();

    }
  }
}


//  }
//}

/*********************************************************************************************************
  END FILE
*********************************************************************************************************/
