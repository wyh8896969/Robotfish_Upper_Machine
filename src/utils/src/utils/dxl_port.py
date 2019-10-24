#!/usr/bin/env python
# encoding:utf-8
from dynamixel_sdk import *
# from register import *
from utils.port_tool import PortTool

BAUD_RATE = 57600
DEVICE_NAME = 'USB <-> Serial Converter'  # 舵机转接线在树莓派上显示的设备名，用于查找端口
PROTOCOL_VERSION = 2.0


class DxlPort:
    def __init__(self):
        self.port = PortTool.get_port(DEVICE_NAME)  # 获取设备端口号
        if self.port is None:
            quit()
        self.portHandler = PortHandler(self.port)
        self.portHandler.setBaudRate(BAUD_RATE)
        if self.portHandler.openPort():
            print('Succeed to open port')
        else:
            print('Failed to open port')
            quit()



class DxlIO(DxlPort):
    """
    舵机控制模块实例化此类即可，包括数据交互句柄
    """
    def __init__(self):
        DxlPort.__init__(self)
        self._packetHandler = PacketHandler(PROTOCOL_VERSION)
        # self._portHandler = DxlPort()
        # self._port = self.portHandler
        self._setup()

    def _setup(self):
        pass

    def read(self, dxl_id, addr, b):
        data, result, error = (None, None, None)
        if b == 1:
            data, result, error = self._packetHandler.read1ByteTxRx(self.portHandler, dxl_id, addr)
        elif b == 2:
            data, result, error = self._packetHandler.read2ByteTxRx(self.portHandler, dxl_id, addr)
        elif b == 4:
            data, result, error = self._packetHandler.read4ByteTxRx(self.portHandler, dxl_id, addr)

        if result != COMM_SUCCESS:
            print('Failed to read data ->%s' % self._packetHandler.getTxRxResult(result))
        elif error != 0:
            print('Error occurred when reading data->%s' % self._packetHandler.getRxPacketError(error))
        return data

    def write(self, dxl_id, addr, b, data):
        result, error = (None, None)
        if b == 1:
            result, error = self._packetHandler.write1ByteTxRx(self.portHandler, dxl_id, addr, data)
        elif b == 2:
            result, error = self._packetHandler.write2ByteTxRx(self.portHandler, dxl_id, addr, data)
        elif b == 4:
            result, error = self._packetHandler.write4ByteTxRx(self.portHandler, dxl_id, addr, data)
        if result != COMM_SUCCESS:
            print('Failed to write data -> addr:%s\tdata:%s' % (addr, data))
            print('%s' % self._packetHandler.getTxRxResult(result))
        elif error != 0:
            print('Error occurred when writing data -> addr:%s\tdata:%s' % (addr, data))
            print('%s' % self._packetHandler.getRxPacketError(error))
        else:
            return True
        return False

if __name__ == '__main__':
    app = DxlIO()
    # data = 
