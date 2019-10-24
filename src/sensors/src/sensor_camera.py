#! /usr/bin/env python
# encoding:utf-8
from picamera import PiCamera
import rospy
from msg.msg import CameraControl
import time
import threading

class Video:
    def __init__(self):
        rospy.init_node('camera', anonymous=True)
        rospy.Subscriber('camera_control', CameraControl, self.run)
        self.camera = PiCamera()
        print "initial done"
        
    def recv_time(self):
        now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        return now
    

        

    def start_RECORD(self):

        
        # self.camera.start_preview()
        # with PiCamera() as self.camera:
            # 视频的分辨率
        if self.camera.closed:
            self.camera = PiCamera()
        self.camera.resolution = (1920, 1080)
        # 视频的旋转
        self.camera.rotation = 180
        # 亮度0-100
        self.camera.brightness = 70
        # 视频帧率
        self.camera.framerate = 25
        # 视频字幕
        self.camera.annotate_text = 'hello'

    
    # 开始录制视频
        self.camera.start_recording('/home/pi/data/video/' + self.recv_time() + r'video.h264')
            # camera.wait_recording(10)
        # 录制时间
        # self.camera.wait_recording(60)
        # sleep(30)
        # camera.capture('data//camera.h264')

    def stop_RECORD(self):
        try:
            self.camera.stop_recording()
            # time.sleep(2)
            self.camera.close()
            print 'stopped'
        except Exception as e:
            print e
        # self.camera.stop_preview()
        
    def main(self):
        while not rospy.is_shutdown():
            pass
        self.camera.close()

    def run(self, signal):
        CMD = signal.mode
        print CMD
        if CMD == 'start_video':
            self.start_RECORD()
        elif CMD == 'stop_video':
            try:
                self.stop_RECORD()
                # threading.Thread(target=RUN.stop_RECORD).start()
            except:
                print("没有开始录像！")
        elif CMD == 'photograph':
            try:
                self.picture()
                # threading.Thread(target=RUN.picture).start()
            except:
                print("正在录像，请先停止！")
    
    def _take_photo(self):
        try:
            
            self.camera.resolution = (1920, 1080)
            # self.camera.start_preview()
            # time.sleep(2)
            pic_name = '/home/pi/data/photo/' + self.recv_time() + r'test.jpg'
            self.camera.capture(pic_name, use_video_port=False)
            # self.camera.stop_preview()
            
        except Exception as e:
            print e

    def picture(self):
        if self.camera.closed:
            self.camera = PiCamera()
        
        # threading.Thread(target=self._take_photo).start()
        self._take_photo()
        time.sleep(1)
        self.camera.close()
        

if __name__ == "__main__":
    app = Video()
    app.main()
    # RUN = Video()

    """while True:
        print('请输入命令')
        CMD = input()

        if CMD == 1:
            RUN.start_RECORD()
                # threading.Thread(target=RUN.start_RECORD).start()
            
        elif CMD == 2:
            RUN.stop_RECORD()
                # threading.Thread(target=RUN.stop_RECORD).start()
        elif CMD == 3:
            
            RUN.picture()
                # threading.Thread(target=RUN.picture).start()
    """