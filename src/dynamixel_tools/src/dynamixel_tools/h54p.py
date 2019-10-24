#!/usr/bin/env python
#encoding:utf-8
from dynamixel_tools.motor import Motor
from dynamixel_tools import register_h54p
from utils.dxl_port import *

packet = DxlIO()
test_id = 1

class H54pMotor(Motor):

    def __init__(self, packet_handler=packet, dxl_id=test_id):
        Motor.__init__(self, packet_handler, register_h54p, dxl_id)
        self._default_velocity = 2900 # unit 0.001 rev/s
        self._top_position = 2048
        self._bottom_position = 0
        self._center_postition = self._top_position
        self._max_velocity = 2900  # max velocity 2900 unit 0.001rev/s refer to emanual
        self.wait_unit = 0.0055
        self.setup()

    def change_veloity(self, velocity):
        """
        修改速度，处于速度控制模式时，修改Goal Velocity寄存器，其他模式时修改Profile Velocity寄存器，
        速度最大值不超过self._max_velocity值
        """
        try:
            velocity = int(velocity)
        except ValueError:
            print('The velocity is not int')
        else:
            if velocity <= self._max_velocity:
                if self._get_operating_mode() == self._reg.MODE_VELOCITY:
                    self._write(self._reg.ADDR_GOAL_VELOCITY, self._reg.BYTE_VELOCITY, velocity)
                else:
                    self._write(self._reg.ADDR_PROFILE_VELOCITY, self._reg.BYTE_VELOCITY, velocity)
            else:
                print('The velocity is out of range!')

    def change_operating_mode(self, mode):
        if self._get_operating_mode() != mode:
            if self._write_eeprom(self._reg.ADDR_OPERATING_MODE, self._reg.BYTE_OPERATING_MODE, mode):
                print('Secceed to change operating mode!')
            else:
                print('Failed to change operating mode!')


    def setup(self):
        self._enable_torque(1)
        self.change_operating_mode(self._reg.MODE_EXT_POS)
        self.goto_position(self._center_postition)
        self.change_veloity(self._max_velocity)

