# -*- coding:utf-8 -*-
import time
import serial.tools.list_ports

ser = serial.Serial()
ser.baudrate = 19200
ser.port = 'COM5'
ser.timeout = 0.5
ser.setDTR(True)
ser.setRTS(False)
print(ser)
ser.open()
print(ser.is_open)

class send_data:

    #run函数使用串口发送传感器数据的
    def run(self,line):
        #file = open('19-06-29_04-49-07_imudata.txt')
        #for line in file:#按行读取
        #time.sleep(1)
        #p = line.strip(' \n').split(' ')
        # print(line)
        ss = ser.write(line.encode())
        print(ss)

    #rec_sensor_data是用来获取传感器总重数据的
if __name__ == '__main__':
    while True:
        AA = send_data()
        AA.run('1')
        time.sleep(2)

