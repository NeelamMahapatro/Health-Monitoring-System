import paho.mqtt.client as mqtt
import time
import requests
import string
def on_connect(client, userdata, flags, rc):
    print("Connected with Main server broker "+str(rc))
    client.subscribe("sensor data")  #client.subscribe("topic2")
    print("Subscribed for sensor data")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    #userdata={msg.topic: str(msg.payload)}
    #resp = requests.post("http://localhost/data.php", params = userdata)
    print("Got")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.14.96.52", 1883, 60)

client.loop_forever()
