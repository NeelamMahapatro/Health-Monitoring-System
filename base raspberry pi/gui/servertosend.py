import paho.mqtt.publish as publish
import paho.mqtt.client as paho
import random, string, time
import serial

broker="10.14.79.58"
port=1883

def on_publish(client,userdata,result):             #create function for callba$
    print("Data sent to server \n")

client1= paho.Client()
client1.on_publish = on_publish 

client1.connect(broker,port)
ser = serial.Serial('/dev/ttyArduino', 115200, 8,'N', 1, timeout=5)

while True:
    data = ser.readline()
    client1.publish("oximeter", data)
    sensor = data.decode("ascii").split(":")
    para = (sensor[0])
    if(para == "airflow"):
        file = open("temphash.text","r")
        hash = file.readline()
        msg = "hashkey: "+hash
        client1.publish("hkey", msg)
        print(msg)  
    print(data)
    print("\n")
    #time.sleep(1)

print ("Done")

