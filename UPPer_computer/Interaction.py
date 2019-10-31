# -*- coding:utf-8 -*-
import serial_com
import DisplayImu
import time
class Data_interaction:

    def Data_Send(self):

        return 1

    def Data_Recv(self):
        recv = serial_com.data_com()  # 调用receive文件中的recv_data()类
        send = DisplayImu.ReadData()
        if recv.OPEN():
            print("连接成功")
            # 调用receive文件中的recv_data()类中的run()函数获取数据
            display_data = recv.run_recv()
            # dis是对接收数据进行格式转换
            dis = display_data.decode('utf-8')
            # p是对数据按空格键分割，保存成list格式，便于取数据
            print(dis)
            # p = dis.strip(' \n').split(' ')
            # len(p)是对p去长度
            # send.RECV_DATA(p)
            # print(len(p))

            # return p

if __name__ == '__main__':
    app = Data_interaction()
    while True:
        app.Data_Recv()
        time.sleep(2)