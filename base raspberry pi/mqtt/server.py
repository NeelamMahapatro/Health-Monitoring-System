import paho.mqtt.publish as publish
import paho.mqtt.client as paho
import random, string, time
import serial

broker="10.14.96.52"
port=1883

def on_publish(client,userdata,result):             #create function for callba$
    print("Data sent to server \n")

client1= paho.Client()
client1.on_publish = on_publish 

client1.connect(broker,port)
ser = serial.Serial('/dev/ttyACM0', 115200, 8,'N', 1, timeout=5)

while True:
    data = ser.readline()
    client1.publish("oximeter", data)
    print (data+"\n")
    time.sleep(1)

print ("Done")

