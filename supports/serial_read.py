import serial

ser = serial.Serial('COM18', 115200, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()

while True:
    data_raw = ser.readline()
    #print(data_raw)
    print(data_raw.decode('utf-8'))
