#! /usr/bin/env python
# encoding:utf-8
# -*- coding:utf-8 -*-
import camera
import threading
class CMD:
    def run(self):
        RUN = camera.video()
        # RUN.start_video()
        threading.Thread(target=RUN.start_video, args=()).start()

    def stop(self,k):
        return k

if __name__ == '__main__':
    RUN = CMD()
    while True:
        print('请输入命令')
        CCMD = input()

        if CCMD == 1:
                RUN.stop(1)
        elif CCMD == 2:
                RUN.run()
        elif CCMD == 3:
                RUN.start_video()

'''
import cv2
import time
import threading

class video:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def recv_time(self):
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        return now

    def run(self):
        # flag = k
        self.cap.set(3, 640)  # 宽
        self.cap.set(4, 480)  # 高
        sz = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        # 为保存视频做准备
        fourcc = cv2.VideoWriter_fourcc(*"DIVX")
        # fourcc = cv2.CV_FOURCC("D", "I", "B", "")
        fps = 25
        out = cv2.VideoWriter('/home/pi/data/video/' + self.recv_time() + r'video.avi', fourcc, fps, sz)
        while self.cap.isOpened():
            # 一帧一帧的获取图像
            ret, frame = self.cap.read()
            if ret is True:
                out.write(frame)

    def stop(self):
        # 释放摄像头资源
        cv2.destroyAllWindows()
        self.cap.release()
        print("关闭成功！")
        # exit()
        # out.release()

if __name__ == '__main__':
    RUN = video()
    # RUN.run(0)
    while True:
        print('请输入命令')
        CMD = input()
        if CMD == 1:
            threading.Thread(target=RUN.run, args=()).start()
            print("程序1已开始……")
        elif CMD == 2:
            RUN.stop()
            # RUN.stop()
            # threading.Thread(target=RUN.run, args=(1, )).start()
            print("程序2已开始……")
        elif CMD == 3:
            start_video()
    '''