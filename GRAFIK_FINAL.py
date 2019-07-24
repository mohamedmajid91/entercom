from matplotlib import pyplot
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyfirmata,socket,math,time


port = 'COM4'
board = pyfirmata.Arduino(port)
it = pyfirmata.util.Iterator(board)
it.start()

a0 = board.get_pin('a:0:i')
a1 = board.get_pin('a:1:i')
a2 = board.get_pin('a:2:i')
a3 = board.get_pin('a:3:i')

n = 501

pData1 = [None] * n
pData2 = [None] * n
pData3 = [None] * n
pData4 = [None] * n

fig, ax = pyplot.subplots()


l1, = ax.plot(pData1)
l2, = ax.plot(pData2)
l3, = ax.plot(pData3)
l4, = ax.plot(pData4)

l1.set_xdata(range(-n + 1, 1))
l2.set_xdata(range(-n + 1, 1))
l3.set_xdata(range(-n + 1, 1))
l4.set_xdata(range(-n + 1, 1))

ax.set(ylim=(0, 1), xlim=(-n + 1, 0))

print(" board.analog[0].enable_reporting()\n","board.analog[1].enable_reporting()\n","board.analog[2].enable_reporting()\n","board.analog[3].enable_reporting()\n\n\n"," Calculating First Integer\n\n\n")
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
board.analog[2].enable_reporting()
board.analog[3].enable_reporting()
time.sleep(5.0)
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

def update(data):

    global host
    global port
    global x1
    global x2
    global y1
    global y2
    board.digital[11].write(0)
    x1=board.analog[0].read()*1000
    y1=board.analog[1].read()*1000
    x2=board.analog[3].read()*1000
    y2=board.analog[2].read()*1000
    x1=math.floor(x1)
    x2=math.floor(x2)
    y1=math.floor(y1)
    y2=math.floor(y2)
    time.sleep(0.01)
    print("***************\nX1=",x1,"\nY1=",y1,"\nX2=",x2,"\nY2=",y2)
    
    pyplot.title(x1)
    board.digital[11].write(1)
    del pData1[0]
    pData1.append(float(a0.read()))
    l1.set_ydata(pData1)
    del pData2[0]
    pData2.append(float(a1.read()))
    l2.set_ydata(pData2)
    del pData3[0]
    pData3.append(float(a2.read()))
    l3.set_ydata(pData3)
    del pData4[0]
    pData4.append(float(a3.read()))
    l4.set_ydata(pData4)
    return l1,l2,l3,l4,
      


ani = animation.FuncAnimation(fig, update, interval=20, blit=True)
plt.show(block=False)

pyplot.show()
    
