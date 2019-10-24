#! /usr/bin/env python
# encoding: utf-8
from utils.io_tool import I2CIO
from utils.sensor import SensorBase
import rospy
from msg.msg import ImuData


I2C_ADDR = 0x50

CMD_ACC_X = 0x34
CMD_GYRO_X = 0x37
CMD_ANGLE_X = 0x3d
CMD_MAG_X = 0x3a
BYTE_MAG = 2
BYTE_ACC = 2
BYTE_GYRO = 2
BYTE_ANGLE = 2
K_ACC = 16.0
K_GYRO = 2000.0
K_ANGLE = 180.0


class JY901(SensorBase):

    def __init__(self, io=None):
        """

        :param io:tools.io.I2CIO
        """
        
        rospy.init_node('imu', anonymous=True)
        self.rate = rospy.Rate(10)
        self._pub = rospy.Publisher('imu',ImuData, queue_size=10)
        self._io = I2CIO(I2C_ADDR, False) if io is None else io
        # print self._io
        SensorBase.__init__(self,self._io, "imu")
        self.msg = ImuData()
        



    def read_data(self):
        """
        节点主程序，汇总imu数据并发布自定义ImuData消息，并写入文件
        """
        while not rospy.is_shutdown():
            acc = self.accelerate()
            ang = self.angle()
            gyro = self.gyro()
            mag = self.mag()
            # 将列表转为字符串，再发布消息
            self.msg.acc = str(acc).lstrip('[').rstrip(']')
            self.msg.ang = str(ang).lstrip('[').rstrip(']')
            self.msg.gyro = str(gyro).lstrip('[').rstrip(']')
            self.msg.mag = str(mag).lstrip('[').rstrip(']')
            data = '{:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f} {:.4f}'.format(
                acc[0],acc[1],acc[2],ang[0],ang[1],ang[2],
                mag[0],mag[1],mag[2],gyro[0],gyro[1],gyro[2]
            )
            rospy.loginfo('[imu]-->read data:{} {} {} {}'.format(acc, ang, gyro, mag))
            self._pub.publish(self.msg)
            self.write_to_file(data)
            # print('[IMU Sensor] Read data --> {}'.format(data))
            self.rate.sleep()
        

    def accelerate(self):
        """
        读取并计算加速度
        """
        raw_acc = [0, 0, 0]
        acc = [0.0, 0.0, 0.0]
        try:
            # 读取原始加速度数据
            for i in range(3):
                raw_acc[i] = self._io.read_block(CMD_ACC_X + i, BYTE_ACC)
        except IOError:
            print('ReadError: accelerate')
        else:
            # 计算加速度
            temp = K_ACC / 32768.0
            for i in range(3):
                acc[i] = round(raw_acc[i] * temp, 6)
                if acc[i] >= K_ACC:
                    acc[i] -= 2 * K_ACC
                    acc[i] = round(acc[i], 6)
        return acc

    def gyro(self):
        """
        读取并计算角速度
        :return:
        """
        raw_gyro = [1, 1, 1]
        gyro = [1.0, 1.0,1.0]
        try:
            for i in range(3):
                raw_gyro[i] = self._io.read_block(CMD_GYRO_X + i, BYTE_GYRO)
        except IOError:
            print("Read Error: gyro")
        else:
            temp = K_GYRO / 32768.0
            for i in range(3):
                gyro[i] = round(raw_gyro[i] * temp, 6)
                if gyro[i] >= K_GYRO:
                    gyro[i] -= 2 * K_GYRO
                    gyro[i] = round(gyro[i], 6)
        return gyro

    def angle(self):
        raw_angle = [0, 0, 0]
        angle = [0.0, 0.0, 0.0]
        try:
            for i in range(3):
                raw_angle[i] = self._io.read_block(CMD_ANGLE_X + i, BYTE_ANGLE)
        except IOError:
            print('Read Error: angle')
        else:
            temp = K_ANGLE / 32768
            for i in range(3):
                angle[i] = round(raw_angle[i] * temp, 6)
                if angle[i] >= K_ANGLE:
                    angle[i] -= 2 * K_ANGLE
                    angle[i] = round(angle[i], 6)
        return angle

    def mag(self):
        """读取磁场"""
        mag = [0.0, 0.0, 0.0]

        try:
            for i in range(3):
                mag[i] = round(self._io.read_block(CMD_MAG_X + i, BYTE_MAG), 6)
        except IOError:
            print('ReadError: magnetic field')
        return mag
    
    
if __name__ == '__main__':
    app = JY901()
    #try:
    app.read_data()
    #except Exception as e:
        #print('[imu]'+ str(e))
