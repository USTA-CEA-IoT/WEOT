//Library and sketch by HomeNode.co
//US915 subband 2
#include "lora_us915sb2.h"
LORA_US915SB2 loraModule(
              "00000000000000000000000000000001", //App. key
              10 //Power index from 5 to 10
);
#include <Wire.h>
#include <SHT2x.h>
void setup()
{
  Wire.begin();
  Serial.begin(9600);
}
 
void loop()
{
  analogReference(DEFAULT); 
  loraModule.joinOTAA();
  delay(4000);
  String tempvaluehex;
  String humvaluehex;
  String metvaluehex;
  String diovaluehex;
  
  while(1){

  //Sensor de CO2
  int sensorValueCO2 = analogRead(A1); 
  float voltajeCO2 = sensorValueCO2*(5000/1024.0); 
  int voltage_diference=voltajeCO2-400;
  float condioxido = voltage_diference*50.0/16.0;
  
  //Sensor de metano
  int sensorValue = analogRead(A0);
  float voltage = sensorValue * (5.0 / 1023.0);//Conversion sensor de CH4
  float conmetano = (voltage*10000)/5;//Conversion sensor CH4
  
  //Sensor de Humedad y Temperatura Si7021 - SHT7021
  float temperatura = (SHT2x.GetTemperature());
  float humedad = (SHT2x.GetHumidity());
  //char data[20];
 
  Serial.println("-------------------------------------------");

  Serial.print("Humedad: ");
  Serial.println(humedad);
  Serial.print("Temperatura(Cº): ");
  Serial.println(temperatura);
  //Sensor de Metano
  Serial.print("Concentración de Metano - CH4 : ");
  Serial.print(conmetano);
  Serial.print("ppm");
  Serial.println();
  //Sensor de Dióxido
  Serial.print("Concentración de CO2:");
  Serial.print(condioxido);
  Serial.println("ppm");

  int newtemp = int(temperatura); 
  int newhum = int(humedad);
  int newmet = int(conmetano);
  int newdio = int(condioxido);
  
 
  String tempvaluehex =String(newtemp,HEX);
  String humvaluehex = String(newhum,HEX);
  String metvaluehex = String(newmet,HEX);
  String diovaluehex = String(newdio,HEX);
  
  //int valorhexa = (newtemp,HEX);
  Serial.print("Valor humedad en Hexa: ");
  Serial.println(humvaluehex);
  
  Serial.print("Valor temperatura en Hexa: ");
  Serial.println(tempvaluehex);
  
  Serial.print("Valor metano en Hexa: ");
  Serial.println(metvaluehex);

  Serial.print("Valor dioxido en Hexa: ");
  Serial.println(diovaluehex);

//  
  String datatemp = "01";//+ diovaluehex;
  String datahumd = "02";//+ humvaluehex;
  String datameth = "03";//+ metvaluehex;
  String datadiox = "04";//+ diovaluehex;

  loraModule.sendDataHex(tempvaluehex); //Send HEX string
  loraModule.sendDataHex(datatemp);
  loraModule.sendDataHex(humvaluehex);
  loraModule.sendDataHex(datahumd);
  loraModule.sendDataHex(metvaluehex);
  loraModule.sendDataHex(datameth);
  loraModule.sendDataHex(diovaluehex);
  loraModule.sendDataHex(datadiox);
 //delay(10000);
  }
}
