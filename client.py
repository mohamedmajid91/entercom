from tabulate import tabulate
import socket
import pyfirmata,socket,math,time
from pyfirmata import INPUT, OUTPUT, PWM
from numpy import interp
import ent3rcomassets
from ent3rcomassets import *

PORTCOM = '/dev/ttyUSB0'
pin=3
dir1=2
host = "127.0.0.1"                       
port = 5555
loss=0
clear_solve()
interface_com_rpIDLE()
new_start()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host, port))
time.sleep(2)

clear_solve()
connection_succes()
new_start()
time.sleep(3)

clear_solve()
#board = pyfirmata.Arduino(PORTCOM)
interface_com_arduIDLE()
new_start()
time.sleep(5)


# 1024 Bayt Giriş:
while True:
    msg = s.recv(1024)
    info = msg.decode('ascii')
    table=(info.split(","))
    uzunluk=len(table)
    if uzunluk==5:

        idpack=table[0]
        x1=table[1]
        x1f=int(x1)




        
        print(tabulate([[loss,table[0],table[1],table[2],table[3],table[4]]], headers=['LOSS PCKTS','TOTAL PCKTS','CHANNEL_1',"CHANNEL_2","CHANNEL_3","CHANNEL_4","CHANNEL_5"]))







        #print(x1f)
        x1fx=interp(x1f,[0,1024],[0,180])
        #servo.write(x1fx)

    else:
        loss=loss+1































"""
    if x1f < 0.5:
        board.digital[dir1].write(0)
        x1fx=x1f-0.5
        x1fx=abs(x1fx)
        x1fx=interp(x1fx,[0,0.540],[0,1])
        print(x1fx*-1)
        board.digital[pin].write(x1fx)
        
    elif x1f > 0.51:
        board.digital[dir1].write(1)
        x1fx=x1f-0.5
        x1fx=interp(x1fx,[0,0.520],[0,1])
        print(x1fx)
        board.digital[pin].write(x1fx)
        
    else:
        x1fx=0
        print(x1fx)
        board.digital[pin].write(x1fx)
"""      
        


















        
