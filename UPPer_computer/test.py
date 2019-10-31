'''
import os
os.system("sudo raspistill -o data//new.jpg")
'''
import PIL.Image
from time import sleep
# from picamera import PiCamera
import time
import serial.tools.list_ports
import base64
import numpy
import PIL.Image
import pickle
import matplotlib
import matplotlib.pyplot

'''
ser = serial.Serial()
ser.baudrate = 19200
ser.port = '/dev/ttyUSB0'
ser.timeout = 1
ser.setDTR(True)
ser.setRTS(False)
print(ser)
ser.open()
print(ser.is_open)
'''
class send_data:
    '''
    #run函数使用串口发送传感器数据的
    def run(self,):

        image_data = open('data//foo.jpg', 'rb').read()
        print("发送中……")
        print(len(image_data))
        ser.write(image_data)
        #print(base64_data)
        print("发送成功")
    '''
    '''
    def recv_img(self):
        # camera = PiCamera()
        camera.resolution = (390, 240)
        camera.start_preview()
        # Camera warm-up time
        # time.sleep(1)
        camera.capture('data//foo.jpg')
        # Read in the image_data
        print("拍照成功 ")
        # image_data = open('data//foo.jpg', 'rb').read()
        # print(image_data)
        self.image_to_array()
    '''
    def image_to_array(self):
        # data_base_path = 'data'
        print("开始将图片转化为数组")
        result = numpy.array([])
        image = PIL.Image.open('data//foo.jpg')
        r, g, b = image.split()  # rgb通道分离
        # 注意：下面一定要reshpae(1024)使其变为一维数组，否则拼接的数据会出现错误，导致无法恢复图片
        r_arr = numpy.array(r).reshape(93600)
        g_arr = numpy.array(g).reshape(93600)
        b_arr = numpy.array(b).reshape(93600)
        # 行拼接，类似于接火车；最终结果：共n行，一行3072列，为一张图片的rgb值
        image_arr = numpy.concatenate((r_arr, g_arr, b_arr))
        result = numpy.concatenate((result, image_arr))

        result = result.reshape(1, 280800)  # 将一维数组转化为n行3072列的二维数组
        print("转化数组over，开始保存为文件")
        # file_path = data_base_path + 'data2.bin'
        with open('data//data2.bin', mode='wb') as f:
            pickle.dump(result, f)
        print("保存成功")
        self.array_to_image()

    def array_to_image(self):
        '''
        从二进制文件中读取数据并重新恢复为图片
        '''
        with open('data//data2.bin', mode='rb') as f:
            arr = pickle.load(f)  # 加载并反序列化数据
        rows = arr.shape[0]  # rows=5
        # pdb.set_trace()
        # print("rows:",rows)
        arr = arr.reshape(rows, 3, 240, 390)
        # print(arr)  # 打印数组
        for index in range(rows):
            a = arr[index]
            # 得到RGB通道
            r = PIL.Image.fromarray(a[0]).convert('L')
            g = PIL.Image.fromarray(a[1]).convert('L')
            b = PIL.Image.fromarray(a[2]).convert('L')
            image = PIL.Image.merge("RGB", (r, g, b))
            # 显示图片
            matplotlib.pyplot.imshow(image)
            matplotlib.pyplot.show()
        # image.save(self.image_base_path + "result" + str(index) + ".png",'png')

if __name__ == '__main__':
    RUN = send_data()
    # camera = PiCamera()
    RUN.array_to_image()
   # while True:
       # RUN.recv_img()

