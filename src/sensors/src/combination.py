#! /usr/bin/env python
# encoding:utf-8
import rospy
from msg.msg import DepthData, ImuData, GpsData, SensorsData
import time

class Combine:
    
    def __init__(self):
        """
        汇总三个传感器的数据并发布整合后的消息
        """
        rospy.init_node('sensor_data')
        self._pub = rospy.Publisher('sensors', SensorsData, queue_size=10)
        self._data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.setup()
        
        
    def setup(self):
        # 初始化数据
        rospy.Subscriber('imu', ImuData, self._imu_data)
        rospy.Subscriber('depth', DepthData, self._depth_data)
        rospy.Subscriber('gps', GpsData, self._gps_data)
        
    def _imu_data(self, data):
        acc =data.acc.split(',')
        ang = data.ang.split(',')
        mag = data.mag.split(',')
        gyro = data.gyro.split(',')
        
        for i in range(3):
            self._data[i] = float(acc[i])
            self._data[i+3] = float(ang[i])
            self._data[i+6] = float(mag[i])
            self._data[i+9] = float(gyro[i])
        
        # print("imu ", str())
        
    def _depth_data(self, data):
        # dep = data
        self._data[12] = data.depth
        self._data[13] = data.pressure
        self._data[14] = data.temp
        
    def _gps_data(self, data):
        self._data[15] = data.height
        self._data[16] = data.lat
        self._data[17] = data.lon
        self._data[18] = data.velocity
        
    def run(self):
        while not rospy.is_shutdown():
            data = str(self._data).lstrip('[').rstrip(']')
            rospy.loginfo(data)
            self._pub.publish(data)
            time.sleep(2)

if __name__ == "__main__":
    app = Combine()
    app.run()
        
        
        