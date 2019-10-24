#!/usr/bin/env python
# encoding:utf-8
import serial.tools.list_ports as list_ports

"""
调用方法PortTool.get_port(device_name)，可根据设备名返回设备所在的端口号，若未找到设备，则返回None
"""


class PortTool:

    @staticmethod
    def get_port(device_name):
        ports = list_ports.comports()
        if len(ports) != 1:
            for port in ports:
                # print(" value:%s"%port)
                if port[1] == device_name:
                    print('Found port:%s' % port[0])
                    return port[0]
        print('No port named %s' % device_name)
        return None

    @staticmethod
    def list_ports():
        ports = list_ports.comports()
        for port in ports:
            print(port)


if __name__ == '__main__':
    # 显示树莓派上串口连接设备的名称和串口号
    PortTool.list_ports()
