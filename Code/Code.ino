
#include <ELClient.h>
#include <ELClientRest.h>
int sensor = 13;
int relay = 12;
char buff[32];
char buff2[32];
String bitcoin_value = "";

unsigned long lastUpdated = millis();
unsigned long samplingTime = 12000;

// Initialize a connection to esp-link using the normal hardware serial port both for
// SLIP and for debug messages.
ELClient esp(&Serial, &Serial);

// Initialize a REST client on the connection to esp-link
ELClientRest rest(&esp);

boolean wifiConnected = false;

// Callback made from esp-link to notify of wifi status changes
// Here we print something out and set a global flag
void wifiCb(void *response)
{
  ELClientResponse *res = (ELClientResponse*)response;
  if (res->argc() == 1)
  {
    uint8_t status;
    res->popArg(&status, 1);

    if (status == STATION_GOT_IP)
    {
      Serial.println("WIFI CONNECTED");  //Wifi gets connected at this place
      wifiConnected = true;
    }
    else
    {

      wifiConnected = false;
      Serial.print("WIFI NOT READY: ");//Wifi not connected,check connection
      Serial.println(status);


    }
  }
}
void setup()
{
  Serial.begin(115200);   // the baud rate here needs to match the esp-link config
  Serial.println("EL-Client starting!");


  // Sync-up with esp-link, this is required at the start of any sketch and initializes the
  // callbacks to the wifi status change callback. The callback gets called with the initial
  // status right after Sync() below completes.
  esp.wifiCb.attach(wifiCb); // wifi status change callback, optional (delete if not desired)
  bool ok;
  do
  {
    ok = esp.Sync();      // sync up with esp-link, blocks for up to 2 seconds
    if (!ok) Serial.println("EL-Client sync failed!");
  } while (!ok);
  Serial.println("EL-Client synced!");

  // Get immediate wifi status info for demo purposes. This is not normally used because the
  // wifi status callback registered above gets called immediately.
  esp.GetWifiStatus();
  ELClientPacket *packet;
  if ((packet = esp.WaitReturn()) != NULL)
  {
    Serial.print("Wifi status: ");
    Serial.println(packet->value);
  }




  //get_bitcoinValue();

  // put your setup code here, to run once:
  pinMode(sensor, INPUT);
  pinMode (relay, OUTPUT);
  //Serial.begin(9600);
  //pinMode(4,INPUT);



}

void loop()
{

  esp.Process();

  if ((millis() - lastUpdated) > samplingTime)
  {
    int moisture = digitalRead(sensor);
    Serial.print("******");
    Serial.print(moisture);
    Serial.println("******");

    if (moisture == HIGH)
    {
      sendEmail();
    }

    lastUpdated = millis();
  }

}


void sendEmail()
{

  int err = rest.begin("maker.ifttt.com");
  if (err != 0)
  {
    Serial.print("REST begin failed: ");
    Serial.println(err);
    while (1) ;
  }
  Serial.println("EL-REST ready");
  delay(1000);
  //replace with your maker channel's API key
  sprintf(buff, "/trigger/soilMoisture/with/key/c1BVwMuv-fI8ryLpLIihJe");// send mail to user
  logToMaker();  //Log to Maker using commands under void LogToMaker()



}

//function to send POST request to Maker channel
void logToMaker()
{
  // process any callbacks coming from esp_link
  esp.Process();
  // if we're connected make an HTTP request
  Serial.print("WIFI State: ");
  Serial.println(wifiConnected);


  Serial.println("wifi connected!!");
  // Request  from the previously set-up server
  rest.get((const char*)buff);

  char response[266];
  uint16_t code = rest.waitResponse(response, 266);
  if (code == HTTP_STATUS_OK)    //check for response for HTTP request
  {
    Serial.println("ARDUINO: GET successful:");
    Serial.println(response);
  }
  else
  {
    Serial.print("ARDUINO: GET failed: ");
    Serial.println(code);
  }



}





