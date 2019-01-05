
import paho.mqtt.client as mqtt
import time
import datetime
import string
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

class sen:
  def __init__(self, pbm, spo2, temp, airflow, body_pos, skin_cond, skin_resist, skin_volt,hkey):
    self.pbm = pbm
    self.spo2 = spo2
    self.temp = temp
    self.airflow = airflow
    self.body_pos = body_pos
    self.skin_cond = skin_cond
    self.skin_resist = skin_resist
    self.skin_volt = skin_volt
    self.hkey = hkey

s1 = sen("","","","","","","","","")

def on_call(sensor,data):
    if(sensor == "pbm"):
        s1.pbm = data

    elif(sensor == "spo2"):
        s1.spo2 = data

    elif(sensor == "temp"):
        s1.temp = data

    elif(sensor == "airflow"):
        s1.airflow = data

    elif(sensor == "hashkey"):
        hkey = data
        try:
            connection = mysql.connector.connect(host='localhost', database='SDN', user='root', password='12345')
            print(type(hkey))
            print("before query")
            sql = "INSERT INTO EpiOne_Data(pbm,spo2,temp,airflow,Hashkey) VALUES (%s, %s,%s, %s,%s )"
            val = (s1.pbm, s1.spo2, s1.temp , s1.airflow, hkey)
            print("After query")
            cursor = connection.cursor()
            result  = cursor.execute(sql,val)
            connection.commit()
            print ("Record inserted successfully into temp table")
        except mysql.connector.Error as error :
            connection.rollback()
            print("Failed inserting record into epionedata table {}".format(error))
        finally:
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
      
def on_connect(client, userdata, flags, rc):
    print("Connected with Main server broker "+str(rc))
    client.subscribe("oximeter")
    client.subscribe("hkey")  #client.subscribe("topic2")
    print("Subscribed for sensor data and hash key")

def on_message(client, userdata, msg):
    #print(msg.topic+"  "+str(msg.payload))
    incoming = str(msg.payload)
    print(incoming)
    if(incoming != "=============================" and incoming != ""):
        #print("Inside")
        sensor, data = incoming.split(":") 
        on_call(sensor,data)



client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.14.79.58", 1883, 60)

client.loop_forever()
