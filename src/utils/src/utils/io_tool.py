#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: 
@file: io
@time: 2019/7/23 9:23
"""
import serial
import binascii
import smbus
from utils.port_tool import PortTool
import threading


class AbstractIO:

    def close(self):
        pass


class I2CIO(AbstractIO):

    def __init__(self, addr, MSB_first=True):
        """

        :param addr:设备地址，十六进制
        :param MSB_first: 读取数据时，高位在前/低位在前
        """
        # AbstractIO.__init__(self)
        self._addr = addr
        self._MSB_first = MSB_first
        try:
            self.i2c = smbus.SMBus(1)
        except Exception as e:
            print('Failed to create i2c IO-->' + str(e))
            quit()

    def write_byte(self, byte_data):
        self.i2c.write_byte(self._addr, byte_data)

    def read_block(self, cmd, block_num):
        """按块读取
        根据预先设定好的读取顺序解算最终数据并返回
        :param cmd: 读取命令（通常为十六进制）
        :param block_num: 读取的字节数（根据具体硬件信息确定）
        """
        d = self.i2c.read_i2c_block_data(self._addr, cmd, block_num)
        # read_i2c_block_data返回值为block_num数量的列表，需要进行合并
        data = 0x00
        if self._MSB_first:
            for i in range(block_num):
                data = data | d[i] << 8 * (block_num - i - 1)
        else:
            for i in range(block_num):
                data = data | d[i] << 8 * i
        return data

    def read_word(self, cmd):
        """读取一个字（两个字节）的数据

        """
        data = self.i2c.read_word_data(self._addr, cmd)
        if self._MSB_first:
            data = ((data & 0xff) << 8) | (data >> 8)
        return data


class SerialIO(AbstractIO):

    def __init__(self, baudrate, port=None, device_name=None):
        """
        串口通信工具， 可通过端口号或设备名其中之一进行连接
        
        Parameters
        ----------
        baudrate : int
            波特率
        port : str, optional
            端口号, by default None
        device_name : str, optional
            设备名, by default None
        """
        self._io = serial.Serial()
        self._io.baudrate = baudrate
        if device_name is not None:
            self._io.port = PortTool.get_port(device_name)
        else:
            self._io.port = port
        self._io.timeout = 1.0

        self._io.open()
        if not self._io.isOpen():
            print('Failed to open serial port!')
        self._io.setRTS(False)
        self._io.setDTR(True)

    def read_asc(self):
        """读取发送端发送的二进制格式的ASCII数据，并将其转换成字符串格式的ASCII数据"""
        l = self._io.inWaiting()
        data = self._io.read(l)
        data = str(binascii.b2a_hex(data))[2:-1]
        return data

    def read(self):
        """ 读取缓存区数据，若无数据，返回None """
        l = self._io.inWaiting()
        
        if l is not 0:
            try:
                
                data = self._io.read(l).decode('utf-8', 'ignore')
                # print data
            except Exception as e:
                # print 'read error' 
                data = None
            l = 0
        else:
            data = None
        return data

    def inWaiting(self):
        """
        是否有数据待接收
        """
        if self._io.inWaiting() != 0:
            return True
        else:
            return False

    def write(self, data):
        """
        写入数据
        
        Parameters
        ----------
        data : str
            待写入数据
        
        Returns
        -------
        int
            数据长度
        """
        length = self._io.write(data.encode('utf-8'))
        # print('Send data :' + data)
        return length
