import tkinter as tk 
import os 
import sys
from PIL import Image, ImageTk 
import random,string, time
import serial


def on_click_pbm():
    print("destroy server py file")
    os.system("sh kill_serverfile.sh")
    time.sleep(2)
    print("pbm clicked")
    root.destroy()
    os.system("python barplot_pbm.py")  

def on_click_spo2():
    print("destroy server py file")
    os.system("sh kill_serverfile.sh")
    time.sleep(2)
    print("spo2 clicked")
    root.destroy()
    os.system("python barplot_spo2.py")

def on_click_temp():
    print("destroy server py file")
    os.system("sh kill_serverfile.sh")
    time.sleep(2)
    print("temp clicked")
    root.destroy()
    os.system("python barplot_temp.py")

def on_click_airflow():
    print("destroy server py file")
    os.system("sh kill_serverfile.sh")
    time.sleep(2)
    print("airflow clicked")
    root.destroy()
    os.system("python barplot_airflow.py")

def on_click(event=None):
    print("image clicked")    

def on_click_ecg():
    button="active"
    print("Not integrated")

def function():
    root.destroy()
    os.system("sh kill_serverfile.sh")
    #os.system("sh kill_recvflag.py")
    os.system("python index.py")

root = tk.Tk()
root.title('Live Plot')
root.geometry("300x250")

#root.geometry("250x200")
#root.configure(background="#D3D9D8")

image = Image.open("bp.png")
photo = ImageTk.PhotoImage(image)
l = tk.Label(root)
l.grid()

image1 = Image.open("spo2.png")
photo1 = ImageTk.PhotoImage(image1)
l1 = tk.Label(root)
l1.grid()

image2 = Image.open("temp.png")
photo2 = ImageTk.PhotoImage(image2)
l2 = tk.Label(root)
l2.grid()

image3 = Image.open("airflow.png")
photo3 = ImageTk.PhotoImage(image3)
l3 = tk.Label(root)
l3.grid()

image4 = Image.open("ecg.png")
photo4 = ImageTk.PhotoImage(image4)
l4 = tk.Label(root)
l4.grid()

b = tk.Button(root, image=photo, command=on_click_pbm, height=70, width=100)
b.grid(row=0,column=0)

b1 = tk.Button(root, image=photo1, command=on_click_spo2, height=70, width=100)
b1.grid(row=0,column=1)

b2 = tk.Button(root, image=photo2, command=on_click_temp, height=70, width=100)
b2.grid(row=0,column=2)

b3 = tk.Button(root, image=photo3, command=on_click_airflow, height=50, width=50)
b3.grid(row=1,column=0)

b4 = tk.Button(root, image=photo4, command=on_click_ecg, height=70, width=100)
b4.grid(row=1,column=1)

#l.bind('close', on_click)
#b5 = tk.Button(root, text="START RECORDING", command=readytosend, font=("bold", 10))
#b5.grid(row=3, column=0)

close = tk.Button(root, text="LOG OUT", command=function, font=("bold", 10))
close.grid(row=3,column=1)

root.mainloop()
