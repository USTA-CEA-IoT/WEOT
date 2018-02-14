	#!/usr/bin/python
from time import localtime,strftime,time,gmtime
import paho.mqtt.subscribe as subscribe
import requests
import json
from datetime import datetime
import base64
from time import sleep
import time
import datetime
import os, time
topics = ['application/9/node/0004a30b001efd26/rx']

m = subscribe.simple(topics, hostname="lora.com.co", retained=False, msg_count=8)

#Funcion para decodificar los datos de base 64 a hexa y luego a decimal

def conversiondec(dato):
	encoded = dato.decode("base64").encode("Hex")
	prefijo="0x"
	result= prefijo+encoded
	resultdec=int(result,0)
	return resultdec

def identificar(numero):
	ww = listadecimal.index(numero)
	dato=listadecimal[ww-1]
	return dato

listadecimal=[]

for a in m:

	json_string = a.payload
	parsed_json = json.loads(json_string)
	data_list=[]
	data_list.append(parsed_json['data'])
	#en datalist se almacenan los 4 datos del json
	#que corresponden a ch4,co2,temp, y hum en base 64
	
	for x in data_list:
		listadecimal.append(conversiondec(x))

dato_temperatura=identificar(1)
dato_humedad=identificar(2)
dato_metano=identificar(3)
dato_dioxido=identificar(4)

lista_final=[dato_temperatura,dato_humedad,dato_metano,dato_dioxido]

file=open('variables.txt','w')

if lista_final[0] == dato_temperatura:

	datot= dato_temperatura
	file.write(str(datot))
	file.write("\n")
	url="https://bucket.usantotomas.edu.co/api/sensors/59c9238a7be12b496b19d8ff/captures?userToken=l9m0o1dempib0p6djerdu0a91t"
	payload={"sensorId": "59c9238a7be12b496b19d8ff", "captureTypeName": "Temperature C", "value": datot, "captureDate": datetime.today().isoformat(" ")}
	headers = {'Content-Type': 'application/json'}
	r=requests.post(url, data=json.dumps(payload),headers=headers, verify=False)
	

	print(datot)

if lista_final[1] == dato_humedad:	
	datoh= dato_humedad
	file.write(str(datoh))
	file.write("\n")
	url="https://bucket.usantotomas.edu.co/api/sensors/59cc2ef97be12b496b19d933/captures?userToken=l9m0o1dempib0p6djerdu0a91t"
	payload={"sensorId": "59cc2ef97be12b496b19d933", "captureTypeName": "Humidity %", "value": datoh, "captureDate": datetime.today().isoformat(" ")}
	headers = {'Content-Type': 'application/json'}

	r=requests.post(url, data=json.dumps(payload),headers=headers,verify=False)

if lista_final[2] == dato_metano:
	
	datom= dato_metano
	file.write(str(dato_metano))
	file.write("\n")
	url="https://bucket.usantotomas.edu.co/api/sensors/59cc2f017be12b496b19d934/captures?userToken=l9m0o1dempib0p6djerdu0a91t"
	payload={"sensorId": "59cc2f017be12b496b19d934", "captureTypeName": "Methane PPM", "value": datom, "captureDate": datetime.today().isoformat(" ")}
	headers = {'Content-Type': 'application/json'}

	r=requests.post(url, data=json.dumps(payload),headers=headers,verify=False)

if lista_final[3] == dato_dioxido:

	datod= dato_dioxido
	file.write(str(dato_dioxido))
	file.write("\n")
	url="https://bucket.usantotomas.edu.co/api/sensors/59cc2f2b7be12b496b19d935/captures?userToken=l9m0o1dempib0p6djerdu0a91t"
	payload={"sensorId": "59cc2f2b7be12b496b19d935", "captureTypeName": "Carbon Dioxide PPM", "value": datod, "captureDate": datetime.today().isoformat(" ")}
	headers = {'Content-Type': 'application/json'}

	r=requests.post(url, data=json.dumps(payload),headers=headers,verify=False)
	

os.environ['TZ'] = 'America/Bogota'
time.tzset()
hora=strftime("%Y-%m-%d %I:%M:%S %p")
file.write(hora)
file.write("\n")
file.close()
