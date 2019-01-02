import serial
from time import sleep
import datetime
from firebase import firebase
import urllib2, urllib, httplib
import json
import os 
from functools import partial

firebase = firebase.FirebaseApplication('https://ioss-b3875.firebaseio.com/', N$
#firebase.put("/uwb", "/t1_pos", "36.00")
#firebase.put("/uwb", "/t2_pos", "12.00")

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    timeout=0.1
    )


ser.write(b'\r\r')
sleep(2)
res=ser.read(100)
#print(res)

def update_firebase(res1):

    data = res1
    #print(data)
    firebase.post("/anchorStatus" , data)


 while True:
    ser.write(b'la\r')
    sleep(2)
    res1=ser.read(100)
    #print(res1)
    
    update_firebase(res1)
    sleep(5)
