# -*- coding:utf-8 -*-
import serial.tools.list_ports
# import Action
import time

BAUDRATE = 19200
# PORT = '/dev/ttyUSB0'
PORT = 'COM3'
TIME_OUT = 0.5
class recv_data:
    def __init__(self, baudrate=BAUDRATE, port=PORT, time_out=TIME_OUT):
        self._baudrate = baudrate
        self._port = port
        self._time_out = time_out
        self._ser = serial.Serial(baudrate=self._baudrate,port=self._port,timeout=self._time_out)
        self._ser.setRTS(False)
        self._ser.setDTR(True)

    def run(self):
        # AC = Action.AC()
        num=self._ser.inWaiting()
        print(num)
        ss = self._ser.readline()
        # ss = ss.decode('utf-8')
        print(ss)
        return ss

    def isOpen(self):
        return self._ser.isOpen()

if __name__ == '__main__':
    se = recv_data()
    while se.isOpen():
        # se = recv_data()
        se.run()
        time.sleep(1)