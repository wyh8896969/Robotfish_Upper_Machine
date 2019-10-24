#!/usr/bin/env python
# -*- coding:utf-8 -*-
import cv2
import time
import sys
import numpy as np
import rospy
from msg.msg import CameraControl
import os

CAMERA = ['photograph', 'start_video', 'stop_video', 'camera_stop']

class photo:

    def __init__(self):
        rospy.init_node('camera')
        self._stop_video = 0
        rospy.Subscriber('camera_control', CameraControl, self._parse)
        self._mode = ''
        self._path = os.path.expandvars('$HOME') + '/robotfish/src/data'
        print(self._path)
        
        # self.cap = cv2.VideoCapture(0)
        # print(self.cap.isOpened())


    def recv_time(self):
        now = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return now

    def _parse(self, data):
        """解析指令"""
        cmd = data.mode
        
        if cmd in CAMERA:
            print("[camera]Received mode :"+ cmd)
            if cmd == 'stop_video':
                self._stop_video = 1
                print('[camera]Stop recording')
            else:
                self._mode = cmd

    def run(self):
        print('[camera]photo')
        cap=cv2.VideoCapture(0)
        print(cap.isOpened())
        #cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        ret ,frame = cap.read()
        path = self._path + '/photo/'
        if not os.path.exists(path):  # 检查路径
            os.makedirs(path)
        cv2.imwrite(path + self.recv_time() + '.jpg',frame)
        cap.release()
        cv2.destroyAllWindows()
        print('[camera]photo done')
    
    def circle(self):
        while not rospy.is_shutdown():
            if self._mode == 'photograph':
                self.run()
                self._mode = ''
            elif self._mode == 'start_video':
                self.REC()
                self._mode = ''
            elif self._mode == 'camera_stop':
                pass
            

    def REC(self):

        video=cv2.VideoCapture(0)#打开摄像头
        print('[camera]Start recording')    
        fourcc = cv2.VideoWriter_fourcc(*'XVID')#视频存储的格式
        fps = video.get(cv2.CAP_PROP_FPS)#帧率
        #视频的宽高
        video.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        video.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        path = self._path + '/video/'
        if not os.path.exists(path):  # 检查路径
            os.makedirs(path)
        out = cv2.VideoWriter(path + self.recv_time() + '.avi', fourcc, 20, (640, 480))#视频存储

        while out.isOpened():
            ret,img=video.read()#开始使用摄像头读数据，返回ret为true，img为读的图像
            if ret is False:#ret为false则关闭
                exit()
            # cv2.namedWindow('video',cv2.WINDOW_AUTOSIZE)#创建一个名为video的窗口
            # cv2.imshow('video',img)#将捕捉到的图像在video窗口显示
            out.write(img)#将捕捉到的图像存储
            #按esc键退出程序(将此处的判断语句改为获取命令信息
            # cv2.waitKey(1)改为recv_cmd == 'stop_RECOR')
            if self._stop_video:
                self._stop_video = 0
                # video.release()#关闭摄像头
                break
        video.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':

    RUN = photo()
    RUN.circle()
    #RUN.run()
    """while True:
        print("请输入命令：")
        CMD = input()
        if CMD == 1:
            RUN.run()
        if CMD == 2:
            exit()
        if CMD == 3:
            RUN.REC()"""
