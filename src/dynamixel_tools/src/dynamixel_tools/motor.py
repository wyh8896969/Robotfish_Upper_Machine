#! /usr/bin/env python
# encoding:utf-8
# from .register_xm540 import *
from dynamixel_tools import register_xm540
from utils.dxl_port import *


class Motor:

    def __init__(self, packet_handler, register, dxl_id=1):
        self._dxl_id = dxl_id  # 舵机id
        self._packet = packet_handler  # 用于与舵机通信的工具包
        self._reg = register  # 定义舵机各个寄存器地址的包
        self._is_enable = 0  # 舵机是否在工作状态
        self._center_position = 0  # 舵机的转动的中心位置

    def _get_operating_mode(self):
        """ 返回当前的操作模式 """
        return self._read_eeprom(self._reg.ADDR_OPERATING_MODE, self._reg.BYTE_OPERATING_MODE)

    def goto_position(self, pos):
        """
        舵机转动到指定位置
        :param pos: int/float
        :return:
        """
        self._write(self._reg.ADDR_GOAL_POSITION, self._reg.BYTE_POSITION, int(pos))

    def _read(self, addr, b):
        """ 读取当前舵机的RAM区数据 """
        return self._packet.read(self._dxl_id, addr, b)

    def _read_eeprom(self, addr, b):
        """
        读取当前舵机EEPROM区数据
        :param addr: register address
        :param b: bytes of data
        :return: data if succeed to read, result messages if failed
        """
        if self._is_enable:
            self._enable_torque(0)
        result = self._packet.read(self._dxl_id, addr, b)
        if not self._is_enable:
            self._enable_torque(1)
        return result

    def _enable_torque(self, cmd):
        """
        使能/停止舵机
        :param cmd:
        :return:
        """
        self._write(self._reg.ADDR_TORQUE_ENABLE, 1, cmd)
        self._is_enable = cmd

    def _write(self, addr, b, data):
        """向RAM区寄存器写入"""
        return self._packet.write(self._dxl_id, addr, b, data)

    def _write_eeprom(self, addr, b, data):
        """ 向EEPROM区写入 """
        if self._is_enable:
            self._enable_torque(0)
        result = self._packet.write(self._dxl_id, addr, b, data)
        if not self._is_enable:
            self._enable_torque(1)
        return result
    
    def get_id(self):
        id = self._read_eeprom(self._reg.ADDR_ID, self._reg.BYTE_ID)
        print("DXL ID is ", id)
        
    def set_id(self, id):
        result = self._write_eeprom(self._reg.ADDR_ID, self._reg.BYTE_ID, id)
        if result:
            print("Succeed to set id to ", id)
        else:
            print("Faild to set id!")

