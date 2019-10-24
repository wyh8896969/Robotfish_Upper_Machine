#! /usr/bin/env python
# encoding:utf-8
import rospy
from msg.msg import GpsData
from utils.io_tool import SerialIO
from utils.sensor import SensorBase


# io = SerialIO(9600, '/dev/ttyAMA0')
BAUDRATE = 9600
PORT = '/dev/ttyAMA0'
DEVICE_NAME = 'USB2.0-Serial'  # gps连接转接板后的设备名

class GPS(SensorBase):

    def __init__(self, io=None):
        """

        gps节点，GPS通过转接板连接USB
        """
        self._io = SerialIO(BAUDRATE, device_name=DEVICE_NAME) if io is None else io
        SensorBase.__init__(self, self._io, 'gps')
        
        self._data = ''
        self._pub = rospy.Publisher('gps', GpsData, queue_size=10)
        rospy.init_node('gps',anonymous=True)
        self.msg = GpsData()
        

    def read_data(self):
        """
        返回解算后的GPS数据
        :return: tuple  (velocity, latitude, logitude)
        """
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self._data = self._io.read_asc()
            #if len(self._data) == 0:
                #print('No data received')
            # 读取格式‘244750524d432c2c562c2c2c2c2c2c2c2c2c2c4e2a35330d0a2447505654472’

            velocity = self._parse_velocity()
            lat, log,height = self._parse_position()
            self.msg.velocity = velocity
            self.msg.lat = lat
            self.msg.lon = log
            self.msg.height = height    
            self._pub.publish(self.msg)
            data = '{:.4f} {:.4f} {:.4f} {:.4f}'.format(velocity, lat, log, height)
            self.write_to_file(data)
            print('[GPS Sensor] Read data --> {}'.format(data))
            rate.sleep()
        rospy.spin()

    def _parse_velocity(self):
        velocity = 0
        try:
            GPS_DATA = str(self._data.encode('utf-8'))
            # 把数据放入数组方便字符串匹配和提取提取
            GPS_DATA = GPS_DATA.strip(' \n').split('0d0a')
            # 接收了所有数据我们对想要的数据提取
            for k in range(len(GPS_DATA)):
                gps_data = GPS_DATA[k]
                # 对想要的字符串匹配(在这个字符串里找到我们想要的速度信息)
                if gps_data[0:12] == '244750524d43':
                    # VEL_Data是我们想要的信息数组，要进一步提取
                    VEL_Data = GPS_DATA[k]
                    # GPS_Velocity是将我们需要的信息按照","分割
                    GPS_Velocity = VEL_Data.strip(' \n').split('2c')
                    # 判断数据是否有效’41‘转译过来是A代表有效
                    if GPS_Velocity[7] != '':
                        velocity = GPS_Velocity[7]
                        ST = ''
                        for i in range(int(len(velocity) / 2)):
                            j = i * 2
                            st = str(velocity[j:j + 2])
                            # 转换成十进制
                            st = int(st, 16)
                            # 转换成字符型
                            st = chr(int(st))
                            ST = ST + st
                        velocity = ST
                        print("速度信息" + velocity)
            return velocity
        except Exception as e:
            print("Error occurred:"+str(e))

    def _parse_position(self):
        lat_data = 0
        log_data = 0
        ST3 = 0
        try:
            GPS_DATA = str(self._data.encode('utf-8'))
            # 把数据放入数组方便字符串匹配和提取提取
            GPS_DATA = GPS_DATA.strip(' \n').split('0d0a')
            # 接收了所有数据我们对想要的数据提取
            for k in range(len(GPS_DATA)):
                gps_data = GPS_DATA[k]
                if gps_data[0:12] == '244750474741':
                    # 从字符串中找到位置信息
                    POSITION_Data = GPS_DATA[k]
                    GPS_Position = POSITION_Data.strip(' \n').split('2c')
                    if GPS_Position[2] != '':
                        # st1、st2、st3分别是纬度、经度和海拔
                        st1 = GPS_Position[2]
                        st2 = GPS_Position[4]
                        st3 = GPS_Position[9]

                        ST1 = ''
                        for i in range(int(len(st1) / 2)):
                            j = i * 2
                            st = str(st1[j:j + 2])
                            # 转换成十进制
                            st = int(st, 16)
                            # 转换成字符型
                            st = chr(int(st))
                            ST1 = ST1 + st

                        ST2 = ''
                        for i in range(int(len(st2) / 2)):
                            j = i * 2
                            st = str(st2[j:j + 2])
                            # 转换成十进制
                            st = int(st, 16)
                            # 转换成字符型
                            st = chr(int(st))
                            ST2 = ST2 + st

                        ST3 = ''
                        for i in range(int(len(st3) / 2)):
                            j = i * 2
                            st = str(st3[j:j + 2])
                            # 转换成十进制
                            st = int(st, 16)
                            # 转换成字符型
                            st = chr(int(st))
                            ST3 = ST3 + st

                        gps_position = ST1 + ' ' + ST2 + ' ' + ST3
                        print("原始经纬度信息" + gps_position)
                        log_data = ''
                        lat_data = ''
                        if ST1 != '':
                            log = ST1.strip(' \n').split('.')
                            lat = ST2.strip(' \n').split('.')
                            if len(log[0]) == 4:
                                DE = ST1[0:2]
                                MI = ST1[2:]
                                MI = float(MI) / 60.0
                                log_data = int(DE) + MI
                                print("纬度信息" + str(log_data))

                            elif len(log[0]) == 5:
                                DE = ST1[0:3]
                                MI = ST1[3:]
                                MI = float(MI) / 60.0
                                log_data = int(DE) + MI
                                print("纬度信息" + str(log_data))

                            if len(lat[0]) == 4:
                                DE = ST2[0:2]
                                MI = ST2[2:]
                                MI = float(MI) / 60.0
                                lat_data = int(DE) + MI
                                print("经度信息" + str(lat_data))

                            elif len(lat[0]) == 5:
                                DE = ST2[0:3]
                                MI = ST2[3:]
                                MI = float(MI) / 60
                                lat_data = int(DE) + MI
                                print("经度信息" + str(lat_data))
            return lat_data, log_data, ST3
        except Exception as e:
            print("Error occurred:"+str(e))

if __name__ == '__main__':
    app = GPS()
    app.read_data()
