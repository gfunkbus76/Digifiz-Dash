/**************************
 *         Author         *
 *      omarCartera       *
 *                        *
 *        5/8/2017        *
 *                        *
 * c.omargamal@gmail.com  *
 **************************/

#include <SPI.h>          //SPI is used to talk to the CAN Controller
#include <mcp_can.h>

MCP_CAN CAN(10);          //set SPI Chip Select to pin 10

unsigned char len = 0;
unsigned char buf[8];
unsigned int canID;

unsigned int engine_rpm;
unsigned char speed_cv;
unsigned char coolant_temp;
unsigned char boost;
unsigned char egt;
unsigned char oil_pressure;
unsigned char fuel;
unsigned char outside_temp;
unsigned char temp;


void setup()
{
  Serial.begin(115200);   //to communicate with Serial monitor

//tries to initialize, if failed --> it will loop here for ever
START_INIT:

    if(CAN_OK == CAN.begin(CAN_500KBPS, MCP_8MHZ))      //setting CAN baud rate to 500Kbps
    {
        Serial.println("CAN BUS Shield init ok!");
    }
    else
    {
        Serial.println("CAN BUS Shield init fail");
        Serial.println("Init CAN BUS Shield again");
        delay(100);
        goto START_INIT;
    }
}


void loop()
{
    if(CAN_MSGAVAIL == CAN.checkReceive())        //check if data coming
    {
        CAN.readMsgBuf(&len, buf);    //read data,  len: data length, buf: data buffer
        canID = CAN.getCanId();       //getting the ID of the incoming message

        if (canID == 0x036)            //reading only our beloved 0xF1 message
        {
          //for the second signal: engine RPM
          engine_rpm = buf[5];
          engine_rpm = engine_rpm << 8;
          temp = buf[6];
          engine_rpm = engine_rpm + temp;

          Serial.print("Engine RPM = ");
          Serial.println(engine_rpm);

                    
          //for the first signal: car speed
          car_speed = buf[0];
          
          Serial.print("Car speed = ");
          Serial.println(car_speed);


          //for the third signal: check engine light
          if((buf[2] & 0x40) >> 6 == 1)
          {
            Serial.println("OIL LIGHT");
          }

          else if((buf[2] & 0x40) >> 6 == 0)
          {
            Serial.println("Turn OFF check engine light");
          }


          //for the fourth signal: oil indicator
          if((buf[2] & 0x80) >> 7 == 1)
          {
            Serial.println("Turn ON Oil indicator");
          }

          else if((buf[2] & 0x80) >> 7 == 0)
          {
            Serial.println("Turn OFF Oil indicator");
          }


          
          Serial.println("\n\n\t*************");
        }
      }
}
