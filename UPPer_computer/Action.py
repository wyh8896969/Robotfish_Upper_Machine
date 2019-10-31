# -*- coding:utf-8 -*-
#import serial_com
#import send
import DisplayImu

class ac ():
    def __init__(self):
        self.model = ''
        self.cmd = ''
    def RECV_MODEL(self, model):
        self.model = model
        print('MODEL' + model)
        #return MODEL

    def SEND_CMD(self, CMD):
        self.cmd = CMD
        sendcmd = DisplayImu.ReadData()
        sendcmd.cmd()
        return CMD

    # 控制机器人前进
    def forward_2(self):
        print('前进2')
        self.SEND_CMD('forward_2')
        return 'forward_2'

    def forward_1(self):
        print('前进1')
        self.SEND_CMD('forward_1')
        return 'forward_1'

    def forward_3(self):
        print('前进3')
        self.SEND_CMD('forward_3')
        return 'forward_3'

    def back(self):
        print('后退')
        self.SEND_CMD('back')
        return 'back'

    def left(self):
        print('左转')
        self.SEND_CMD('left')
        return 'left'

    def right(self):
        print('右转')
        self.SEND_CMD('right')
        return 'right'

    def rising(self):
        print('上升')
        self.SEND_CMD('rising')
        return 'rising'

    def diving(self):
        print('下潜')
        self.SEND_CMD('diving')
        return 'diving'

if __name__ == '__main__':
    AA = ac()
    AA.forward_2()




