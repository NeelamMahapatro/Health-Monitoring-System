import mysql.connector

mydb = mysql.connector.connect( host="localhost",  user="root", passwd="12345", database="SDN" ) 
mycursor = mydb.cursor() 

email = "neelammahapatro36@gmail.com"
password="123456"
sql = "SELECT * FROM Patient WHERE Email = %s AND password = %s" 
adr = (email,password, )

mycursor.execute(sql, adr) 
myresult = mycursor.fetchall()


for x in myresult:
  print(x)
