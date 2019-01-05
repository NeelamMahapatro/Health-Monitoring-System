import paho.mqtt.publish as publish 
import paho.mqtt.client as paho
import time
import os
import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import serial
import time
import string
import tkinter as Tk
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ser = serial.Serial('/dev/ttyArduino', 115200, 8, 'N', 1, timeout=5)

broker="10.14.79.58"
port=1883

def on_publish(client,userdata,result): #create function for callba$
    print("Data sent to server \n")

client1= paho.Client() 
client1.on_publish = on_publish
client1.connect(broker,port)

def backtoicon():
    root.destroy()
    os.system("sh kill_serverfile.sh")
    os.system("python after_login.py")    

class Window:
    
    def __init__(self,master):
        
        frame = Tk.Frame(master)
        self.fig = plt.figure(figsize=(6,4), dpi=50)
        self.b1 = Tk.Button(frame,text="Back", command=backtoicon, foreground="blue")
        self.b1.pack(side=Tk.LEFT)
        self.ax = self.fig.add_subplot(1,1,1)
        self.ax.grid()
        self.ax.set_ylim([0,40])
        print ("<<<<<<")
        print (xar,yar)
        print (">>>>>>")
        self.rect = self.ax.bar(xar,yar,width=5)
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
        frame.pack()

    def animate(self,i):
        xar = 0
        yar = 0.0
        data = ser.readline().strip()
        print(data)
        client1.publish("oximeter", data)
        if(data!="b'============================='"):
           sensor  = data.decode("ascii").split(":")
           para = (sensor[0])
           val = (sensor[-1])

           if (para == "pbm"):
            
             yar=float(val)
             xar=i
             print ("***yay***")
             print (yar)
             self.rect = self.ax.bar(xar,yar,width=2) 
             self.ax.set_xlim([i-5,i+5])
           
           if(para == "airflow"):
             file = open("temphash.text","r")
             hashk = file.readline()
             msg = "hashkey: "+hashk
             client1.publish("hkey", msg)
             print(msg)
             file.close()

xar = 0
yar = 0.0

root = Tk.Tk()
root.title('Pulse Live plot')
app = Window(root)
ani = animation.FuncAnimation(app.fig, app.animate, interval=100, blit=False)
root.mainloop()
