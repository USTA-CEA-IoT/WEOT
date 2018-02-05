#!/usr/bin/python
from time import localtime,strftime,time
import paho.mqtt.subscribe as subscribe
import requests
import json
from datetime import datetime
import base64
from time import sleep
import time

topics = ['application/9/node/0004a30b001efd26/rx']

m = subscribe.simple(topics, hostname="lora.com.co", retained=False, msg_count=8)

#Funcion para decodificar los datos de base 64 a texto

def conversion(string):
	out_data=string.decode('base64')
	#print(out_data)
	return str(out_data)

#For to parse the json associate to each mqtt message

lista_decodificada=[]

for a in m:

	json_string = a.payload
	parsed_json = json.loads(json_string)
	data_list=[]
	data_list.append(parsed_json['data'])
	#en datalist se almacenan los 4 datos del json
	#que corresponden a ch4,co2,temp, y hum en base 64


	b = parsed_json['data']
	decimal=' '.join([ str(ord(c)) for c in b.decode('base64') ])
	#print("Datos parseados en base 64:", b)
		
	lista_decodificada.append(decimal)
	#print(lista_decodificada)
	# x=["dato1","dato2","dato3"]

def identificar(numero):
	ww = lista_decodificada.index(numero)
	dato=lista_decodificada[ww-1]
	#print("el dato es: ",dato)
	return dato

dato_temperatura=identificar('1')
dato_humedad=identificar('2')
dato_metano=identificar('3')
dato_dioxido=identificar('4')

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
	print(datoh)

if lista_final[2] == dato_metano:
	
	datom= dato_metano
	file.write(str(dato_metano))
	file.write("\n")
	url="https://bucket.usantotomas.edu.co/api/sensors/59cc2f017be12b496b19d934/captures?userToken=l9m0o1dempib0p6djerdu0a91t"
	payload={"sensorId": "59cc2f017be12b496b19d934", "captureTypeName": "Methane PPM", "value": datom, "captureDate": datetime.today().isoformat(" ")}
	headers = {'Content-Type': 'application/json'}

	r=requests.post(url, data=json.dumps(payload),headers=headers,verify=False)
	print(datom)

if lista_final[3] == dato_dioxido:

	datod= dato_dioxido
	file.write(str(dato_dioxido))
	file.write("\n")
	url="https://bucket.usantotomas.edu.co/api/sensors/59cc2f2b7be12b496b19d935/captures?userToken=l9m0o1dempib0p6djerdu0a91t"
	payload={"sensorId": "59cc2f2b7be12b496b19d935", "captureTypeName": "Carbon Dioxide PPM", "value": datod, "captureDate": datetime.today().isoformat(" ")}
	headers = {'Content-Type': 'application/json'}

	r=requests.post(url, data=json.dumps(payload),headers=headers,verify=False)
	print(datod)
	
hora=strftime("%Y-%m-%d %H:%M:%S",localtime())
file.write(hora)
file.write("\n")
file.close()
