from pyfirmata import Arduino, util
import time,math
import matplotlib.pyplot as plt
from drawnow import *

values = []
plt.ion()


port = "COM4"
board = Arduino(port)
it = util.Iterator(board)
it.start()
print(" board.analog[0].enable_reporting()\n","board.analog[1].enable_reporting()\n","board.analog[2].enable_reporting()\n","board.analog[3].enable_reporting()\n\n\n"," Calculating First Integer\n\n\n")
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
board.analog[2].enable_reporting()
board.analog[3].enable_reporting()
time.sleep(2.0)
x1=board.analog[0].read()*1000
y1=board.analog[1].read()*1000
x2=board.analog[3].read()*1000
y2=board.analog[2].read()*1000
x1=math.floor(x1)
x2=math.floor(x2)
y1=math.floor(y1)
y2=math.floor(y2)
print("***************\nFirst Integer :\nX1=",x1,"\nY1=",y1,"\nX2=",x2,"\nY2=",y2,"\n***************\n\n\n\n\n\n\n\n")
time.sleep(1.0)

for i in range(0,101):
    values.append(0)
    
def plotValues():
    plt.grid(True)
    plt.plot(values, 'rx-', label='values')
    plt.legend(loc='upper right')

def calc():
    global x1
    global valueInInt
    global valueRead
    x1=board.analog[0].read()*1000
    x1=math.floor(x1)
    valueRead = x1
    valueInInt = int(valueRead)
    print(valueInInt)

def append():
    global x1
    global valueInInt
    global valueRead
    values.append(valueInInt)
    values.pop(0)
    drawnow(plotValues)

while True:
    board.digital[11].write(1)
    calc()
    append()
    board.digital[11].write(0)

