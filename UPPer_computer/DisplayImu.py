# -*- coding:utf-8 -*-
import serial.tools.list_ports
# from PIL import Image
# import numpy as np
from PyQt5.QtGui import QPixmap

from imu import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
# import Action
import time

ser = serial.Serial()
port_list = list(serial.tools.list_ports.comports())
for i in range(0, len(port_list)):
    port_list_0 = list(port_list[i])
    port_0 = port_list_0[0]
    ser.port = port_0
ser.baudrate = 19200
#ser.port = port_0
ser.timeout = 0.5
ser.setDTR(True)
ser.setRTS(False)
print(ser)
ser.open()

class ReadData(QtCore.QThread):
    signal = QtCore.pyqtSignal(list)

    def __init__(self):
        super(ReadData, self).__init__()
        # self.recv = serial_com.data_com()

    def run_recv(self):
        num = ser.inWaiting()
        print(num)
        ss = ser.readline()
        print(ss)
        return ss

    def run_send(self, cmd):
        # time.sleep(1)
        ss = ser.write(cmd.encode('utf-8'))
        print('发送成功！')
        print(ss)

    def run(self):

        while True:
            try:
                # recv = serial_com.data_com()
                # 调用receive文件中的recv_data()类
                while ser.isOpen():
                    print("连接成功")
                    # 调用receive文件中的recv_data()类中的run()函数获取数据
                    display_data = self.run_recv()
                    # dis是对接收数据进行格式转换
                    dis = display_data.decode()
                    # p是对数据按空格键分割，保存成list格式，便于取数据
                    p = dis.strip(' \t\n').split(' ')
                    # len(p)是对p去长度
                    print(len(p))
                    if len(p) == 19:
                        p.insert(19, '连接成功')
                        self.signal.emit(p)
                        time.sleep(2)

                    else:
                        p = []
                        p.insert(0, '0'), p.insert(1, '0'), p.insert(2, '0')
                        p.insert(3, '0'), p.insert(4, '0'), p.insert(5, '0')
                        p.insert(6, '0'), p.insert(7, '0'), p.insert(8, '0')
                        p.insert(9, '0'), p.insert(10, '0'), p.insert(11, '0')
                        p.insert(12, '0'), p.insert(13, '0'), p.insert(14, '0')
                        p.insert(15, '0'), p.insert(16, '0'), p.insert(17, '0'),
                        p.insert(18, '0'), p.insert(19, '连接成功')

                        print(p)
                        self.signal.emit(p)
                        time.sleep(2)
            except:
                print("连接失败")
                p = []
                p.insert(0, '0'), p.insert(1, '0'), p.insert(2, '0')
                p.insert(3, '0'), p.insert(4, '0'), p.insert(5, '0')
                p.insert(6, '0'), p.insert(7, '0'), p.insert(8, '0')
                p.insert(9, '0'), p.insert(10, '0'), p.insert(11, '0')
                p.insert(12, '0'), p.insert(13, '0'), p.insert(14, '0')
                p.insert(15, '0'), p.insert(16, '0'), p.insert(17, '0')
                p.insert(18, '0'), p.insert(19, '连接失败')
                self.signal.emit(p)
                time.sleep(2)

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):

        super(MyWindow,self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer(self)
        self.update_data = ReadData()
        # self.update_data = serial_com.data_com()
        self.update_data.signal.connect(self.read_data)
        self.update_data.start()
        self.command()
        self.timer = QTimer(self)
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
        self.recv_data()
        self.Open_img()

    def read_data(self,p):

            self.lineEdit.setText(str(p[0]))
            self.lineEdit_2.setText(str(p[1]))
            self.lineEdit_3.setText(str(p[2]))
            self.lineEdit_11.setText(str(p[9]))
            self.lineEdit_12.setText(str(p[10]))
            self.lineEdit_10.setText(str(p[11]))
            self.lineEdit_8.setText(str(p[6]))
            self.lineEdit_7.setText(str(p[7]))
            self.lineEdit_9.setText(str(p[8]))
            self.lineEdit_5.setText(str(p[3]))
            self.lineEdit_4.setText(str(p[4]))
            self.lineEdit_6.setText(str(p[5]))
            self.lineEdit_14.setText(str(p[13]))
            self.lineEdit_13.setText(str(p[12]))
            self.lineEdit_20.setText(str(p[14]))
            self.lineEdit_23.setText(str(p[17]))
            self.lineEdit_24.setText(str(p[16]))
            self.lineEdit_17.setText(str(p[15]))
            self.lineEdit_22.setText(str(p[18]))
            self.label_30.setText(str(p[19]))
            print(p)
            print(p[1])
            return p
    def command (self):
        self.pushButton.clicked.connect(self.forward)
        self.pushButton_2.clicked.connect(self.back)
        self.pushButton_3.clicked.connect(self.left)
        self.pushButton_4.clicked.connect(self.right)
        self.pushButton_5.clicked.connect(self.rising)
        self.pushButton_6.clicked.connect(self.diving)
        self.pushButton_7.clicked.connect(self.show_data)
        self.pushButton_10.clicked.connect(self.photograph)
        self.pushButton_11.clicked.connect(self.start_video)
        self.pushButton_12.clicked.connect(self.stop_video)

    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString()
        self.label_29.setText(""+ text)

    # 从combo Box中获取数据
    def recv_data(self):
        # velocity = self.comboBox.currentText()
        swim_mode = self.comboBox_2.currentText()
        # SEND_SWIM_MODEL = Action.ac()
        # SEND_SWIM_MODEL.RECV_MODEL(str(swim_mode))
        return swim_mode

    def Open_img(self):
        # imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        #imgName= Image.open('data//timg.jpg')
        pix = QPixmap('data//timg.jpg')
        #jpg = QtGui.QPixmap(imgName).scaled(self.label_31.width(), self.label_31.height())
        self.label_31.setPixmap(pix)

    # 显示获取的数据输入到text Edit中
    # velocity和swim_mode 为速度和游泳模式，根据不同来判断发送的指令
    def show_data(self):
        swim_mode = self.recv_data()
        # print("当前的速度为：" + velocity)
        # 连接SIN_action文件
        if swim_mode == 'SIN模式':
            print('SIN')
        # 连接CPG_action文件
        elif swim_mode == 'CPG模式':
            print('CPG')
        print("当前的游泳模式为：" + swim_mode)
        self.textEdit.setText("当前的游泳模式为：" + swim_mode + '\n' + "Q为前进（速度1），W为前进（速度2）" + '\n' + "E为前进（速度3）,A为左转，S为后退" + '\n' + "D为右转，Shift为上升，Ctrl为下潜")

        # return swim_mode

    # 检测键盘回车按键
    def keyPressEvent(self, event):
        SEND = ReadData()
        print("按下：" + str(event.key()))
        # 举例
        if (event.key() == Qt.Key_Shift):
            SEND.run_send('up')
            print('测试：上升')
            self.lineEdit_16.setText('上升')
        if (event.key() == Qt.Key_Control):
            SEND.run_send('dive')
            print('测试：下潜')
            self.lineEdit_16.setText('下潜')
        if (event.key() == Qt.Key_W):
            # SEND.run_send('forward_2')
            SEND.run_send('forward')
            print('测试：前进')
            # W键默认速度2
            self.lineEdit_16.setText('前进(速度2)')
        elif (event.key() == Qt.Key_Q):
            SEND.run_send('forward_1')
            print('测试：前进')
            # Q键速度1
            self.lineEdit_16.setText('前进(速度1)')
        elif (event.key() == Qt.Key_E):
            SEND.run_send('forward_3')
            print('测试：前进')
            # E键速度3
            self.lineEdit_16.setText('前进(速度3)')
        if (event.key() == Qt.Key_S):
            # SEND.run_send('back')
            SEND.run_send('stop')
            print('测试：后退')
            self.lineEdit_16.setText('后退')
        if (event.key() == Qt.Key_A):
            SEND.run_send('left')
            print('测试：左转')
            self.lineEdit_16.setText('左转')
        if (event.key() == Qt.Key_D):
            SEND.run_send('right')
            print('测试：右转')
            self.lineEdit_16.setText('右转')

    def forward(self):
        SEND = ReadData()
        # SEND.run_send('forward_2')
        SEND.run_send('forward')
        self.lineEdit_16.setText(str("前进"))

    def back(self):
        SEND = ReadData()
        # SEND.run_send('back')
        SEND.run_send('stop')
        self.lineEdit_16.setText(str("后退"))

    def left(self):
        SEND = ReadData()
        SEND.run_send('left')
        self.lineEdit_16.setText(str("左转"))

    def right(self):
        SEND = ReadData()
        SEND.run_send('right')
        self.lineEdit_16.setText(str("右转"))

    def rising(self):
        SEND = ReadData()
        SEND.run_send('up')
        self.lineEdit_16.setText(str("上升"))

    def diving(self):
        SEND = ReadData()
        SEND.run_send('dive')
        self.lineEdit_16.setText(str("下潜"))

     # 拍照
    def photograph(self):
        SEND = ReadData()
        SEND.run_send('photograph')
        self.lineEdit_16.setText(str("正在拍照"))

    # 开始录制
    def start_video(self):
        SEND = ReadData()
        SEND.run_send('start_video')
        self.lineEdit_16.setText(str("开始录制"))

    # 停止录制
    def stop_video(self):
        SEND = ReadData()
        SEND.run_send('stop_video')
        self.lineEdit_16.setText(str("停止录制"))

if __name__ == "__main__":  # 主程序调用类以及显示
    app = QtWidgets.QApplication(sys.argv)
    ui = MyWindow()
    ui.show()
    sys.exit(app.exec_())


