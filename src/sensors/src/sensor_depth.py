#! /usr/bin/env python
# encoding:utf-8
import rospy
from utils.io_tool import I2CIO
from msg.msg import DepthData
from utils.sensor import SensorBase
import time

MS_Reset = 0x1e
# 压强值数模转换命令
MS_Convert_D1_256 = 0x40

# 温度值数模转换命令
MS_Convert_D2_256 = 0x50

OSR_256, OSR_516, OSR_1024, OSR_2048, OSR_4096, OSR_8192 = range(6)

# 读取数据命令
MS_ADC_Read = 0x00
# 读取寄存器值命令
MS_PROM_Read = 0xa0
# 水密度
DENSITY_FRESHWATER = 997
DENSITY_SALTWATER = 1029
# 压强单位转换(原始单位为 mbar)
UNITS_Pa = 100.0
UNITS_hPa = 1.0
UNITS_kPa = 0.1
UNITS_mbar = 1.0
UNITS_bar = 0.001
UNITS_psi = 0.014503773773022
# 温度单位转换（原始为摄氏度）
UNITS_Centigrade = 1
UNITS_Farenheit = 2
UNITS_Kelvin = 3

MS_ADDR = 0x76

class MS5837(SensorBase):

    def __init__(self, io=None):
        """

        压力传感器节点
        """
        self._pub = rospy.Publisher('depth', DepthData, queue_size=10)
        rospy.init_node('depth', anonymous=True)
        self._io = I2CIO(MS_ADDR) if io is None else io
        
        # self._io = io
        self._pressure = 0
        self._temperature = 0
        self._pre_pressure = 0  # 用于计算深度
        self._c = []  # 存储出厂校准值
        self.msg = DepthData()
        SensorBase.__init__(self, self._io, 'pressure')
        # self.init()   # 初始化
        

    def _reset(self):
        self._io.write_byte(MS_Reset)
        time.sleep(0.1)

    def _convert_pressure(self, over_sampling=OSR_8192):
        """发送压力数据的数模转换命令"""
        self._io.write_byte(MS_Convert_D1_256 + over_sampling)
        # 等待时间与采样频率有关
        time.sleep(2.5e-6 * 2 ** (8 + over_sampling))

    def _convert_temperature(self, over_sampling=OSR_8192):
        """令传感器对温度进行数模转换"""
        self._io.write_byte(MS_Convert_D2_256 + over_sampling)
        time.sleep(2.5e-6 * 2 ** (8 + over_sampling))

    def _calibration_para(self):
        """读取传感器的出厂校准值"""
        # c所有校准值的列表，用于循环校验
        for i in range(7):
            ci = self._io.read_word(MS_PROM_Read + 2 * i)
            self._c.append(ci)

        crc = (self._c[0] >> 12) & 0x000f
        if crc != self._crc4(self._c):
            print('PROM read error, crc failed')
            return False
        return True

    def _crc4(self, prom):
        """
        计算校验和
        :param prom: 校准值的列表
        :return: 循环检验和
        """
        n_rem = 0
        prom[0] = (prom[0] & 0x0fff)
        prom.append(0)

        for i in range(16):
            if i % 2 == 1:
                n_rem ^= ((prom[i >> 1]) & 0x00ff)
            else:
                n_rem ^= (prom[i >> 1]) >> 8

            for n_bit in range(8, 0, -1):
                if n_rem & 0x8000:
                    n_rem = (n_rem << 1) ^ 0x3000
                else:
                    n_rem = (n_rem << 1)
        n_rem = ((n_rem >> 12) & 0x000f)
        return n_rem ^ 0x00

    def init(self):
        """
        调用MS5837().setup()时执行
        """
        self._reset()
        self._calibration_para()
        self._convert_temperature()
        d2 = self._io.read_block(MS_ADC_Read, 3)
        self._convert_pressure()
        d1 = self._io.read_block(MS_ADC_Read, 3)
        self._calculate_pressure(d1, d2)
        # 读取大气压
        self._pre_pressure = self._pressure


    def read_data(self):
        """读取温度与压强的测量值"""
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            self._convert_temperature()
            d2 = self._io.read_block(MS_ADC_Read, 3)
            self._convert_pressure()
            d1 = self._io.read_block(MS_ADC_Read, 3)
            self._calculate_pressure(d1, d2)
            self.msg.depth = float('%.6f' % self.depth())
            rospy.loginfo(self.msg.depth)
            self.msg.pressure = round(self.pressure(), 6)
            self.msg.temp = self.temperature()
            self._pub.publish(self.msg)
            data = '{:.4f} {:.4f} {:.4f}'.format(self.depth(), self.pressure(), self.temperature())
            self.write_to_file(data)
            print('[Pressure Sensor] Read data --> {}'.format(data))
            rate.sleep()

    def _calculate_pressure(self, d1, d2):
        """计算压强值"""
        dT = d2 - self._c[5] * 256
        temp = 2000 + dT * self._c[6] / 8388608

        off = self._c[2] * 65536 + (self._c[4] * dT) / 128
        sens = self._c[1] * 32768 + (self._c[3] * dT) / 256
        self._pressure = (d1 * sens / 2097152 - off) / 8192
        if (temp / 100) < 20:
            ti = 3 * (dT * dT) / 8589934592
            offi = 3 * ((temp - 2000) ** 2) / 2
            sensi = 5 * ((temp - 2000) ** 2) / 8
            if (temp / 100) < -15:
                offi = offi + 7 * ((temp + 1500) ** 2)
                sensi = sensi + 4 * ((temp + 1500) ** 2)
        else:
            ti = 2 * (dT ** 2) / 137438953472
            offi = ((temp - 2000) ** 2) / 16
            sensi = 0

        off2 = off - offi
        sens2 = sens - sensi

        temp2 = (temp - ti) / 100
        p2 = (((d1 * sens2) / 2097152 - off2) / 8192) / 10
        self._pressure = p2
        self._temperature = temp2

    def depth(self, units=UNITS_Pa, density=DENSITY_FRESHWATER):
        """计算深度值，默认单位 米"""
        offset = self._pre_pressure * units
        d = ((self._pressure * units) - offset) / (density * 9.80665)
        return float(d)

    def pressure(self, unit=UNITS_Pa):
        return float(self._pressure * unit)

    def temperature(self, unit=UNITS_Centigrade):
        degC = self._temperature
        if unit == UNITS_Farenheit:
            return (9.0 / 5.0) * degC + 32
        elif unit == UNITS_Kelvin:
            return degC - 273
        return round(float(degC), 6)


if __name__ == '__main__':
    app = MS5837()
    app.read_data()