#include <dht11.h>
#define DHT11PIN 6

dht11 DHT11;
int sensorVals[] = {0,0,0}; 

void setup()
{
  Serial.begin(9600);
 
}

void loop()
{
  Serial.println();

  int chk = DHT11.read(DHT11PIN);

  sensorVals[0] = (int)DHT11.humidity;
  sensorVals[1] = (int)DHT11.temperature;
  sensorVals[2] = analogRead(0);

  if(sensorVals[2] < 200)
  {
    sensorVals[2] = 0;
  }else{
    sensorVals[2] = (sensorVals[2]-200)/3;
  }
  

  Serial.print(sensorVals[0]);
  Serial.print(",");
  Serial.print(sensorVals[1]);
  Serial.print(",");
  Serial.print(sensorVals[2]);
  Serial.println("");
  delay(2000);

}
