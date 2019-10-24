#! /usr/bin/env python
# encoding:utf-8
import RPi.GPIO as gpio
import rospy
from msg.msg import MotionControl

# 引脚定义
EN = 27  # 使能，高电平正常
DR = 17  # 高电平正转
VE = 22  # 调速信号，向其输入PWM
# 推进器V-引脚接地
FREQ = 100

class Thrust:
    def __init__(self):
        """
        
        推进器节点，接收MotionControl消息，目前只有简单的控制
        
        """
        rospy.init_node('thruster')
        self.init()
        # self._freq = 0  # 初始频率
        self._ve = gpio.PWM(VE, FREQ)
        self._sub = rospy.Subscriber('motion_signal', MotionControl, self.set_mode)
        rospy.on_shutdown(self.close)
        self._mode = ''  # 初始状态
        self._changed = False

    def init(self):
        # 设置gpio引脚模式
        gpio.setmode(gpio.BCM)
        gpio.setwarnings(False)
        # 设置引脚工作模式
        gpio.setup(EN, gpio.OUT)
        gpio.setup(DR, gpio.OUT)
        gpio.setup(VE, gpio.OUT)
        # 引脚初始化
        gpio.output(EN, 0)  # 初始化
        gpio.output(DR, 1)
    
    def run(self):
        
        while not rospy.is_shutdown():
              # 使能
            if self._changed:
                if self._mode == 'forward':
                # 前进
                    self.change()
                elif self._mode == 'left':
                    # 左转
                    self.change(90)
                elif self._mode == 'right':
                    # right
                    self.change(80)
                elif self._mode == 'dive':
                    # dive
                    self.change(70)
                elif self._mode == 'up':
                    # up
                    self.change(60)
                else:
                    self.stop()
                self._changed = False  # 标志位清零

    def set_mode(self, data):
        print('thruster changed mode '+data.motion)
        if data.motion != self._mode:  # 模式改变
            self._mode = data.motion
            self._changed = True


    def change(self, dutycycle=100):
        """
        通过占空比调节转速
        """
        gpio.output(EN, 1)
        # self._ve.ChangeFrequency(FREQ)
        self._ve.start(dutycycle)
        # self._freq = freq        
    
    def stop(self):
        # self._ve.stop()
        gpio.output(EN, 0)
        # gpio.cleanup()

    def close(self):
        gpio.output(EN, 0)
        gpio.cleanup()


if __name__ == "__main__":
    app = Thrust()
    app.run()
    # app.stop()
    """while True:
        cmd = raw_input("input frequency('q' to stop):")
        if cmd != 'q':
            try:
                cmd = int(cmd)
                app.change(cmd)
            except ValueError:
                app.stop()
                quit()
        else:
            app.stop()
            quit()"""

    


