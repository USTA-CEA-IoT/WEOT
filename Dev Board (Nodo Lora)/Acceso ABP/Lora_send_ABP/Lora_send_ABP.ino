//#include <stdlib.h>
#include "lora_us915sb2.h"
//Declaración de información para el envío de datos por lora
LORA_US915SB2 loraModule(
              "067473f4", //Device Address
              "0992a02e2562bb8f6e63a02883148807", //Network Session Key
              "1e88d870e59c0aa45a80541b155d5dfa", //App. Session Key
              "0000000000000001", //App. EUI
              10 //Power index from 5 to 10
);
#include <Wire.h>
#include <SHT2x.h>
 
void setup()
{
  Wire.begin();
  Serial.begin(9600);
  analogReference(DEFAULT); 

}
 
void loop()
{
  
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
  
  //Condiciones sensor CO2
 
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
  //delay(5000);
    //Imprime concentración de CO2 
  //Serial.println("----------------------------------");
   
 
  //ENVIO POR LORA
  loraModule.joinABP();
  //delay(1000);
  
  //Serial.println(tempvaluehex);
  //Serial.println(conmetano);
  
  //delay(2000);
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

//Función Itoa
//  itoa(newtemp,data,16); 
//  Serial.print("Valor en Hexa con itoa -->");
//  Serial.println(data);
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
