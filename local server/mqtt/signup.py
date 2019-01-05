import time
import datetime
import string
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import json
import hashlib
import paho.mqtt
import paho.mqtt.publish as publish
import paho.mqtt.client as paho

broker="10.14.79.58"
port=1883

def on_publish_signin(client,userdata,result):             #create function for callba$
    print("Signin flag sent to raspberry pi \n")

client1= paho.Client()
client1.on_publish = on_publish_signin

client1.connect(broker,port)

def signup(data):
    try:
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        date, time_ = timestamp.split(" ")
        date= str(date)
        time_ = str(time_)
        print(type(date))
        print(type(time_))
        connection = mysql.connector.connect(host='localhost', database='SDN', user='root', password='12345')
        print("before query")
        name =str(data['name'])
        email = str(data['emailid'])
        password = str(data['password'])
        contact = str(data['contactnumber'])
        x = hashlib.sha1(str.encode(name+email+contact))
        hashkey = x.hexdigest()
        print(hashkey)
        if(data['usertype'] == "Paramedic"):
            print("Before query")
            #print(type(usertype))
            sql = "INSERT INTO Paramedic (ParaID, ParaName, ParaAddress,Email,Password,ContactNo,Specialization) VALUES (%s, %s,%s, %s,%s, %s,%s)"
            val = ("1234",name," ",email,password,contact," ") 
        else:
            sql = "INSERT INTO Patient(EpiOne, Stethoscope, PID, Pname, Paddress, Pdob, Email, Password, Gender, BloodGroup, Allocated, Alloc_date, Alloc_time,ContactNo, Hashkey, doctor_assigned) VALUES (%s, %s,%s, %s,%s, %s,%s,%s, %s,%s, %s,%s, %s,%s, %s, %s )"
            val = ("1","0","1234" ,name," " ," ",email ,password," "," ","1",date,time_,contact,hashkey, " ")
        print("After query")
        cursor = connection.cursor()
        result  = cursor.execute(sql, val)
        connection.commit()
        print ("Record inserted successfully into temp table")
        client1.publish("signupresult", "1")
        client1.publish("hashkey",key)
    except mysql.connector.Error as error :
        client1.publish("signupresult", "0")
        connection.rollback()
        print("Failed inserting record into Patient  table {}".format(error))
    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def signin(data):
    try:
        connection = mysql.connector.connect(host='localhost', database='SDN', user='root', password='12345')
        mycursor = connection.cursor()
        print("before query")
        email_ = str(data['email'])
        password = str(data['password'])
        print("Email and Password: "+email_+" "+password)
        print(data['usertype'])
        usertype = data['usertype']
        print("Before query")
        if(usertype == "Paramedic"):
            sql = "SELECT * FROM Paramedic WHERE Email = %s AND password = %s"
            adr = (email_,password, )
        elif(usertype == "Patient"):
            sql = "SELECT * FROM Patient WHERE Email = %s AND password = %s"
            adr = (email_,password, )
        print("After query")
        mycursor.execute(sql, adr)
        records = mycursor.fetchall()
        print("Total number of rows in table", mycursor.rowcount)
        print ("Printing each row's column values i.e.  developer record")
        key = " "
        for row in records:
            print("email = ", row[6])
            print("Hashkey = ",row[14])
            key = row[14]
        connection.commit()
        print ("Login successfully")
        #time.sleep(3)
        client1.publish("signinresult", "1")
        client1.publish("hashkey",key)
    except mysql.connector.Error as error :
        connection.rollback()
        print("Failed record into table {}".format(error))
        client1.publish("signinresult", "0")
    finally:
        if(connection.is_connected()):
            mycursor.close()
            connection.close()
            print("MySQL connection is closed")
    

def on_connect(client, userdata, flags, rc):
    print("Connected with Main server broker "+str(rc))
    client.subscribe("signup")  #client.subscribe("topic2")
    client.subscribe("signin")
    print("Subscribed for signup and signin data from raspberry pi")

def on_message(client, userdata, msg):
    #print(msg.topic+"  "+str(msg.payload))
    incoming = str(msg.payload)
    print(str(msg.payload))
    data = json.loads(incoming)
    print(data['usertype'])
    if(msg.topic == "signup"):
        signup(data)
    if(msg.topic == "signin"):
        signin(data)

client = paho.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.14.79.58", 1883, 60)

client.loop_forever()
