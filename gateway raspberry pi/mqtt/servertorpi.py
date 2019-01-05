import paho.mqtt.client as mqtt
import time

broker1= #global ip address of server
port1= 1883

broker2= "172.24.1.1"
port2= 1883

def on_publish(client2, userdata, result):
        print("Data is published to the Raspberry pi broker.......")

def on_connect(client1, userdata, flags, rc):
        print("Connected with raspberry pi broker "+str(rc))
        client1.subscribe("signinresult")
        client1.subscribe("signupresult")
        client1.subscribe("hashkey")
        

def on_message(client1, userdata, msg):
        print(msg.topic+" "+str(msg.payload)+"from main server")
        client2.publish(msg.topic, str(msg.payload))

client1 = mqtt.Client()
client2 = mqtt.Client()

client1.on_connect = on_connect
client1.on_message = on_message 

client2.on_publish = on_publish

client1.connect(broker1, port1, 60)
client2.connect(broker2, port2)

client1.loop_forever()

