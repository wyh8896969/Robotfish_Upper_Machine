# -*- coding:utf-8 -*-
from imu import Ui_MainWindow

class ac ():
    def __init__(self):
        self.u=Ui_MainWindow()
    def forword(self):#控制机器人前进

        print('前进')
        return '前进'

    def back(self):

        print('后退')
        return '后退'

    def left(self):

        print('左转')
        return '左转'

    def right(self):

        print('右转')
        return '右转'

    def rising(self):

        print('上升')
        return '上升'

    def diving(self):

        print('下潜')
        return '下潜'

app = ac()
