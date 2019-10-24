#!/usr/bin/env python
# encoding:utf-8
from dynamixel_tools.motor import Motor
from dynamixel_tools import register_xm540
from utils.dxl_port import DxlIO

class DxlXM540Motor(Motor):

    def __init__(self, dxl_id, packet_handler):
        """

        :param dxl_id:
        :param packet_handler: an instance of PacketHandler
        """
        # self._reg = register_xm540
        Motor.__init__(self, packet_handler, register_xm540, dxl_id)
        self.operating_mode = self._get_operating_mode()
        self._default_velocity = 1000
        self._default_mode = self._reg.MODE_EXT_POSI
        self._max_velocity = 1048
        self._top_position = 2048
        self._bottom_position = 0
        self._center_position = self._top_position
        self.wait_unit = 0.0055
        self.setup()

    def backto_center(self):
        self.goto_position(self._center_position)

    def reverse_center(self, center=None):
        if center is None:
            if self._center_position == self._top_position:
                self._center_position = self._bottom_position
            else:
                self._center_position = self._top_position
        else:
            self._center_position = center
        self.backto_center()

    def change_veloity(self, velocity):
        """
        修改速度，处于速度控制模式时，修改Goal Velocity寄存器，其他模式时修改Profile Velocity寄存器，
        速度最大值不超过self._max_velocity值
        :param velocity:
        :return:
        """
        try:
            velocity = int(velocity)
        except ValueError:
            print('The velocity is not int')
        else:
            if velocity <= self._max_velocity:
                if self.operating_mode == self._reg.MODE_VELOCITY:
                    self._write(self._reg.ADDR_GOAL_VELOCITY, self._reg.BYTE_VELOCITY, velocity)
                else:
                    self._write(self._reg.ADDR_PROFILE_VELOCITY, self._reg.BYTE_VELOCITY, velocity)
            else:
                print('The velocity is out of range!')

    def change_operating_mode(self, mode):

        if self._get_operating_mode() != mode:
            if self._write_eeprom(self._reg.ADDR_OPERATING_MODE, self._reg.BYTE_OPERATING_MODE, mode):
                self.operating_mode = mode
                print('Secceed to change operating mode!')
            else:
                print('Failed to change operating mode!')

    def rotate_around_center(self, position):
        pos = int(self._center_position + position)
        self._write(self._reg.ADDR_GOAL_POSITION, self._reg.BYTE_POSITION, pos)

    def goto_degree(self, degree):
        """
        11.38 position/°
        :param degree:
        :return:
        """
        position = int(degree * 11.38) + self._center_position
        self._write(self._reg.ADDR_GOAL_POSITION, self._reg.BYTE_POSITION, position)

    def setup(self):
        """
        Execute once instance is created, enable torque, change operating mode to extend position mode
        :return:
        """

        self._enable_torque(self._reg.TORQUE_ENABLE)
        self.change_operating_mode(self._reg.MODE_EXT_POSI)
        # set to max velocity
        self.change_veloity(self._default_velocity)

if __name__ == "__main__":
    io = DxlIO()
    app = DxlXM540Motor(1, io)
    app.get_id()
    # print("id ", id)
    