# -*- coding:utf-8 -*-
# serial_com文件主要用来传输数据和命令
import time
import serial.tools.list_ports

BAUDRATE = 19200
PORT = 'COM5'
TIME_OUT = 1


class data_com:
    def __init__(self, baudrate=BAUDRATE, port=PORT, time_out=TIME_OUT):
        self._baudrate = baudrate
        self._port = port
        self._time_out = time_out
        self._ser = serial.Serial(baudrate=self._baudrate, port=self._port, timeout=self._time_out)
        self._ser.setRTS(False)
        self._ser.setDTR(True)

    # run_recv函数主要用来接收下位机发过来的数据
    def run_recv(self):
        num = self._ser.inWaiting()
        print(num)
        ss = self._ser.read(num)
        print(ss)
        return ss

    # run_send函数主要用来发送命令（由上位机发向下位机）
    def run_send(self, cmd):
        # time.sleep(1)
        ss = self._ser.write(cmd.encode('utf-8'))
        print(ss)

    def OPEN(self):
        return self._ser.isOpen()

    def close(self):
        print('closed')
        self._ser.close()


if __name__ == '__main__':
    se = data_com()
    print(se.OPEN())
    # se.close()
    try:
        while se.OPEN():
            # se = recv_data()
            se.run_recv()
            time.sleep(0.5)

    except KeyboardInterrupt:
        pass
    finally:
        se.close()
