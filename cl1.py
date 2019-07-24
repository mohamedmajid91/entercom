import socket
import pyfirmata,socket,math,time
from pyfirmata import INPUT, OUTPUT, PWM
from numpy import interp

port = '/dev/ttyUSB0'
pin=3
dir1=2
print("\n\nRaspberry Pi Control Center\nAttempting To Connect Ardunino Nano\n\nON "+port+" PORT\n")

board = pyfirmata.Arduino(port)


# soket nesne kurulumu
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# server adres
host = "127.0.0.1"                       

port = 1234

# sunucu bağlantısı
s.connect((host, port))                               
print("\nSucces!")
servo = board.get_pin('d:3:s')
time.sleep(5)
# 1024 Bayt Giriş:
while True:
    msg = s.recv(2048)
    info = msg.decode('ascii')
    table=(info.split(","))
    uzunluk=len(table)
    if uzunluk==2:

        idpack=table[0]
        x1=table[1]
        x1f=int(x1)
        print(x1f)
        x1fx=interp(x1f,[0,1024],[0,180])
        servo.write(x1fx)

    else:
        print('Packet Loss')

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
        


















        
