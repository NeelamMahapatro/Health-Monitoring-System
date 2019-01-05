from tkinter import *
from tkinter import ttk
import sys
import os
import tkinter
import paho.mqtt.publish as publish
import paho.mqtt.client as paho
import random, string, time
import json
import serial
import time
import hashlib
import string
from tkinter import messagebox
global temp2

def validate_up(P):
    signupbutn.config(state=(NORMAL if P else DISABLED))
    return True

def validate_in(P):
    loginbutton.config(state=(NORMAL if P else DISABLED))
    return True

ser = serial.Serial('/dev/ttyNano', 9600, 8, 'N', 1, timeout=5)

broker = "10.14.79.58"
port = 1883

def on_publish(client, userdata, result):
    print("Data has been sent to server")

client1 = paho.Client()   # client which sends signin and signup data to databse server
client1.on_publish = on_publish

#client1.connect(broker, port)
creds='tempfile.temp'

root=Tk()
root.title('Welcome to SDN')
root.geometry("350x250")
root.configure(background="blue")
nb = ttk.Notebook(root)
ttk.Style().configure("Notebook")
tab2 = ttk.Frame(nb)
tab1 = ttk.Frame(nb)

nb.add(tab2,text='Sign In')
nb.add(tab1,text='Sign Up')

def fpsignin():
   p=str(1)
   p="\'"+p+",\'"
   ser.write(p.encode(),)
   msg = ser.readline()
   temp1=msg.decode("utf-8")
   if (temp1.startswith("ID:")):
       temp2=temp1.strip()
       print (temp2)
       file = open("signup_logs.txt","r")
       print("Reading from file...")
       while True:
           data = file.readline()
           if(data == ""):
               break
           id, key = data.split(",")
           if(id == temp2):
               print("key found from file: "+key)
               file1 = open("temphash.text", "w")
               file1.write(key)
               file1.close()
               print("logging you in...")
               root.destroy()
               os.system("python after_login.py")
               break
       file.close()
   top = Toplevel()
   top.title('INFO')
   Message(top, text=msg, padx=20, pady=20).pack()
   top.after(3000, top.destroy)  
   print (msg)

  

label_9=Label(tab2,text="Email Id",foreground="blue")
label_9.grid(row=3,column=0,sticky=W)
labelfont = (30)
label_10=Label(tab2,text="Password",foreground="blue")
label_10.grid(row=4,column=0,sticky=W)
labelfont = (30)
label_13=Label(tab2,text="User Type",foreground="blue")
label_13.grid(row=2,column=0,sticky=W)
labelfont = (30)
label_14=Label(tab2,text="Fingerprint",foreground="blue")
label_14.grid(row=6,column=0,sticky=W)
labelfont = (30)
label_or = Label(tab2,text="OR",foreground="blue")
label_or.grid(row=5,column=1)

vcmd1=tab2.register(validate_in)
entry_9=Entry(tab2)
entry_9.grid(row=3,column=3,columnspan=3,sticky=E)
entry_9.focus_set()
entry_10=Entry(tab2,show='*',validate='key',validatecommand=(vcmd1,'%P'))
entry_10.grid(row=4,column=3,columnspan=3,sticky=E)
entry_10.focus_set()
fpbutton=Button(tab2,text="Put finger & Click",width=17,command=fpsignin,foreground="blue")
fpbutton.grid(row=6,column=3,sticky=E)
variable2 = StringVar(tab2)
variable2.set("-Select-")
q = OptionMenu(tab2,variable2,"Paramedic","Patient")
q.grid(row=2,column=3,columnspan=2,sticky=E)
q.config(foreground="blue")
q["menu"].config()


def savesignin():
    e8= variable2.get()
    e9=entry_9.get()
    e10=entry_10.get()
    point_data ={"usertype":e8, "email":e9 ,"password":e10}
    data = (json.dumps(point_data))
    print(data)
    try:
        client1.connect(broker, port)
        client1.publish("signin",data)
        root.destroy()
        #os.system("python recvflag.py")        
    except: 
        client1.publish("signin",data)
        root.destroy()
        #os.system("python recvflag.py")


loginbutton=Button(tab2,text="LOGIN",width=17,state=DISABLED,command=savesignin,foreground="blue")
loginbutton.grid(row=8,column=1,rowspan=1)
loginbutton.place(relx=0.27,rely=0.75)

def fpsignup():
  p=str(2)
  p="\'"+p+",\'"
  ser.write(p.encode(),)
  msg2 = ser.readline()
  temp1=msg2.decode("utf-8")
  if (temp1.startswith("ID:")):
      e1=entry_1.get()
      e3=entry_2.get()
      e5=entry_5.get()
      x = hashlib.sha1(str.encode(e1+e3+e5))
      hashkey = x.hexdigest()
      file=open("signup_logs.txt","a")
      temp=temp1.strip()+","+hashkey+"\n"
      file.write(temp)
  top = Toplevel()
  top.title('INFO')
  Message(top, text=msg2, padx=20, pady=20).pack()
  top.after(3000, top.destroy)
  print (msg2)
  

variable = StringVar(tab1)
variable.set("-Select-") # default value

w = OptionMenu(tab1, variable,"Paramedic","Patient")
w.grid(row=2,column=2,columnspan=3,sticky=E)
w.config(foreground="blue")
w["menu"].config()

    
label_0=Label(tab1,text="User Type",foreground="blue")
label_0.grid(row=2,column=0,sticky=W)
labelfont = (10)
    
label_1=Label(tab1,text="Name",foreground="blue")
label_1.grid(row=3,column=0,sticky=W)
labelfont = (10)
    
#label_2=Label(tab1,text="Fingerprint",foreground="blue")
#label_2.grid(row=4,column=0,sticky=W)
#labelfont = (10)
    
label_3=Label(tab1,text="Email Id",foreground="blue")
label_3.grid(row=5,column=0,sticky=W)
labelfont = (10)
    
label_4=Label(tab1,text="Password",foreground="blue")
label_4.grid(row=6,column=0,sticky=W)
labelfont = (10)
    
#label_5=Label(tab1,text="Reenter Password",foreground="blue")
#label_5.grid(row=7,column=0,sticky=W)
#labelfont = (10)
    
label_7=Label(tab1,text="Contact No.",foreground="blue")
label_7.grid(row=9,column=0,sticky=W)
labelfont = (10)
    
vcmd=tab1.register(validate_up)
entry_1=Entry(tab1)
entry_1.grid(row=3,column=2,columnspan=3,sticky=E)
entry_1.focus_set()
fpbutton1=Button(tab1,text="Click here \n to \n Register \n Fingerprint",height=5,width=7,command=fpsignup,foreground="blue")
fpbutton1.place(relx=0.72,rely=0.18)

entry_2=Entry(tab1)
entry_2.grid(row=5,column=2,columnspan=3,sticky=E)
entry_2.focus_set()
entry_3=Entry(tab1,show='*')
entry_3.grid(row=6,column=2,columnspan=3,sticky=E)
entry_3.focus_set()
#entry_4=Entry(tab1,show='*')
#entry_4.grid(row=7,column=2,columnspan=3,sticky=E)
entry_5=Entry(tab1,validate='key',validatecommand=(vcmd,'%P'))
entry_5.grid(row=9,column=2,columnspan=3,sticky=E)
entry_5.focus_set()
      
def savesignup():
    e0=variable.get()
    e1=entry_1.get()
    e2="15332384rtufh"
    e3=entry_2.get()
    e4=entry_3.get()
    e5=entry_5.get()
    #root.destroy()
    point_data ={"usertype":e0 , "name":e1, "fingerprint":e2, "emailid":e3 ,"password":e4 ,"contactnumber":e5}
    print(point_data)
    data = (json.dumps(point_data))
    try:
        client1.connect(broker, port)
        client1.publish("signup",data)
    except:
        client1.publish("signup",data)

signupbutn=Button(tab1,text="SUBMIT",state=DISABLED,command=savesignup,width=17,foreground="blue")
signupbutn.grid(row=20,rowspan=1)
signupbutn.place(relx=0.22,rely=0.75)


nb.pack(expand=1, fill='both')
    
root.mainloop()

