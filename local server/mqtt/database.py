import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
import datetime
import time

ts = time.time()
timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
x, data = timestamp.split(" ") 

#print(type(data))

try:
    connection = mysql.connector.connect(host='localhost', database='fp', user='root', password='12345')
    x="123445"
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    x, y = timestamp.split(" ")     
    sql_insert_query = ("INSERT INTO `temp`(pbm,spo2,temp,airflow,body_pos,skin_cond, skin_resist, skin_volt) VALUES ({},{},{},{},{},{},{},{},{})".format(x,x,x,x,x,x,x,x,y))
    cursor = connection.cursor()
    result  = cursor.execute(sql_insert_query)
    connection.commit()
    print ("Record inserted successfully into temp table")
except mysql.connector.Error as error :
    connection.rollback() #rollback if any exception occured
    print("Failed inserting record into python_users table {}".format(error))
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


