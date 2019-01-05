import time 
import paho.mqtt.client as mqtt 
import string 
import os
import sys

def on_connect(client, userdata, flags, rc):
    print("Connected with Main server broker "+str(rc))
    client.subscribe("signinresult")
    client.subscribe("signupresult")
    client.subscribe("hashkey") #client.subscribe("topic2")
    print("Subscribed for signin and signup flag and hashkey") 

def on_message(client, userdata,msg):
    print(msg.topic+" "+str(msg.payload))
    #userdata={msg.topic: str(msg.payload)} resp = 
    #requests.post("http://localhost/data.php", params = userdata)
    print("Got") 
    if(msg.topic == "signinresult"):
        if(str(msg.payload)=="b'1'"):
            print("successfully login... directing for sending sensor data...")
            os.system("python after_login.py")
        else:
            print("Login failed... Login again")
            os.system("python index.py")
    if(msg.topic == "hashkey"):
        print(str(msg.payload))
        file = open("temphash.text","w")
        s = str(msg.payload)
        s = s[2:]
        hashkey = s[:len(s)-1] 
        file.write(hashkey)
        file.close()
    if(msg.topic == "signupresult"):
        if(str(msg.payload)=="b'1'"):
            print("successfully registered..... directing for sending sensor data..")
            os.system("python after_login.py")
        elif(str(msg.payload)=="b'0'"):
            print("Register again")
            os.system("python index.py")
     


client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 

client.connect("10.14.79.58", 1883, 60)
client.loop_forever()
