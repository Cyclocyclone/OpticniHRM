import serial
import numpy as np
from datetime import datetime
from csv import writer

#port in baud rate naprave
port = 'COM3'
BR = 115200


#int serial
ser = serial.Serial(port, BR, timeout=10)
print(ser.read(2))
while(1):
    s = ser.read_until()
    try:
        s = "".join(map(chr, s))
        s = s.replace(',1', '')
        s = s.replace('\r', '')
        s = s.replace('\n', '')
        s = int(s)

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        buff = [current_time, s]
        print(buff)

        with open('HRMLog.csv', 'a') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(buff)
            f_object.close()
    except:
        print("Ni signala")

    
