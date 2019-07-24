#!/usr/bin/python3
import socket
from time import sleep
import pyfirmata,socket,math,time
from numpy import interp
port = 'COM3'
board = pyfirmata.Arduino(port)
it = pyfirmata.util.Iterator(board)
it.start()

ayir="\n**************************"
lapse = 0
# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "0.0.0.0"                          
port = 1234                                           
# bind to the port
serversocket.bind((host, port))                                  
# queue up to 5 requests
serversocket.listen(5)                                           

##########################################
#         -Analog Hazırlık-              #
##########################################


board.digital[6].write(1)
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
board.analog[2].enable_reporting()
board.analog[3].enable_reporting()
print("\n##########################################\nboard.analog[0].enable_reporting()\nboard.analog[1].enable_reporting()\nboard.analog[2].enable_reporting()\nboard.analog[3].enable_reporting()\n##########################################\n\nCalculating First Integer :\n")
time.sleep(5)
##########################################
x1=board.analog[0].read()*1000
y1=board.analog[1].read()*1000
x2=board.analog[3].read()*1000
y2=board.analog[2].read()*1000
x1=math.floor(x1)
x2=math.floor(x2)
y1=math.floor(y1)
y2=math.floor(y2)
print("##########################\nFirst Integer :\nX1=",x1,"\nY1=",y1,"\nX2=",x2,"\nY2=",y2,"\n##########################\n\nBağlantı Bekleniyor...\n")
time.sleep(1.0)
board.digital[6].write(0)
##########################################


while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      
   print("Code 202 OK From pi/home/denizaltı_cl1.py %s" % str(addr))
   time.sleep(5)
   while True:
      lapse=lapse+1
      lapsestr=str(lapse)
      lapsestr1=lapsestr+". packed send OK"
      board.digital[11].write(1)
      x1=board.analog[0].read()*1000
      x1=math.floor(x1)
      time.sleep(0.038)
      x1str=str(x1)
      x2str=str(x2)
      y1str=str(y1)
      y2str=str(y2)
      inf2="ID="+lapsestr+","+x1str
      print(inf2)
      clientsocket.send(inf2.encode('ascii'))
      """print(lapsestr1)"""
      board.digital[11].write(0)
