#! /usr/bin/env python
# encoding:utf-8
from msg.msg import *
from utils.io_tool import SerialIO
import rospy
import time
import serial.tools.list_ports

DEVICE_NAME = 'CP2102 USB to UART Bridge Controller'
BAUDRATE = 19200

MOTION = ['forward', 'left', 'right', 'dive', 'up', 'stop']
CAMERA = ['photograph', 'start_video', 'stop_video', 'camera_stop']

class Transceiver:
    
    def __init__(self):
        # 发布胸鳍控制信号
        # self._pec_pub = rospy.Publisher('pec_controller', PecControl, queue_size=10)
        self._pec_pub = rospy.Publisher('motion_signal', MotionControl, queue_size=10)
        # self._pec_msg = MotionControl()  # 胸鳍控制信号
        self._camera_pub = rospy.Publisher('camera_control', CameraControl, queue_size=10)
        self.data = ''  # 将要发送的数据
        rospy.init_node('transceiver')  # 初始化节点
        # 使用RF200
        self._io = SerialIO(BAUDRATE, device_name=DEVICE_NAME)
        rospy.Subscriber('sensors', SensorsData, self._send_data)  # 收到传感器数据后，转入发送程序
        
    def setup(self):
        pass
        
        
    def run(self):
        while not rospy.is_shutdown():
            receive = self._io.read()
            if receive is not None:
                self._parse_data(receive)
                # rospy.loginfo(receive)
            if self.data != '':
                # 有数据需要发送，发送完后清空待发送数据空间
                self._io.write(self.data)
                self.data = ''
                
    def _send_data(self, data):
        """将传感器数据放入待发送缓存"""
        self.data = data.data +'\t\n'
                
    def _parse_data(self, data):
        if data in MOTION:  # 收到运动控制
            print('transceiver received motion control:'+data)
            pec_msg = MotionControl()
            pec_msg.motion = data
            self._pec_pub.publish(pec_msg)    # 发布消息
        elif data in CAMERA:  # 收到相机命令
            print('transceiver received camera control:'+data)
            camera_cmd = CameraControl()
            camera_cmd.mode = data
            self._camera_pub.publish(camera_cmd)
        else:
            print ("Unknown Command:" + data)
        
if __name__ == "__main__":
    app = Transceiver()
    app.run()
    # app._send_data()
        