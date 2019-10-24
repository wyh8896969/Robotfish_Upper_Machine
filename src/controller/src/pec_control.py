#! /usr/bin/env python
# encoding:utf-8

"""暂时用不上
"""
from msg.msg import PecControl
import rospy
from utils.io_tool import SerialIO

DEVICE_NAME = 'CP2102 USB to UART Bridge Controller'
BAUDRATE = 19200
DEFAULT_MODE = 'stop'
class PecController:
    
    def __init__(self):
        self._pub = rospy.Publisher("pec_controller", PecControl, queue_size=10)    # 话题发布者
        self._msg = PecControl()    # 消息对象
        rospy.init_node("pec_controller")   # 初始化节点
        self._io = SerialIO(BAUDRATE, device_name=DEVICE_NAME)
        self._cmd = 'stop'   # 初始化命令，开始时命令舵机停止
        
        
    def run(self):
        while not rospy.is_shutdown():
            cmd = self._io.read()     # 读取指令
            
            if cmd is not None and self._cmd != cmd:
                print(cmd)
                if cmd == 'stop':
                    self._msg.mode = 0  # 停止
                elif cmd == 'forward':
                    self._msg.mode = 1  # 前进
                elif cmd == "left":
                    self._msg.mode = 2  # 左转
                elif cmd == 'right':
                    self._msg.mode = 3  # 右转
                elif cmd == 'dive':
                    self._msg.mode = 4  # 下潜
                elif cmd == 'up':
                    self._msg.mode = 5  # 上升
                else:
                    self._msg.mode = -1
                self._pub.publish(self._msg)    # 发布消息
                
                self._cmd = cmd
                
if __name__ == '__main__':
    app = PecController()
    app.run()        
        