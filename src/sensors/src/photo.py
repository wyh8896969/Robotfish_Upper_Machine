#! /usr/bin/env python
# encoding:utf-8
# -*- coding:utf-8 -*-

import cv2
import time
import sys
import numpy

class Photo:

    def recv_time(self):
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        return now

    def photo(self):
        capture = cv2.VideoCapture()
        ref, frame = capture.read()
        # frame = frame[:,::-1,:]
        cv2.imwrite('/home/pi/data/photo/' + self.recv_time() + r'photo.jpg', frame)
        # self.capture.release()
        print("ok")