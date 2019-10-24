#! /usr/bin/env python
# encoding:utf-8
from msg.msg import *

import rospy

"""
暂时不需要使用
"""

def imu_data(data):
    rospy.loginfo('Recieved data :\n angle:{}\nacc:'.format(data.ang))
    
def depth_data(data):
    rospy.loginfo('Recieved data:\n{}'.format(data.depth))
    
def reciever():
    rospy.init_node('receiver', anonymous=True)
    rospy.Subscriber('imu', ImuData, imu_data)
    rospy.Subscriber('depth', DepthData,depth_data )
    rospy.spin()
    
if __name__ == '__main__':
    reciever()