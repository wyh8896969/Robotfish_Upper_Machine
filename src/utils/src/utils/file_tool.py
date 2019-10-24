# encoding: utf-8
"""
@version: 1.0
@author: 
@file: filetool
@time: 2019/7/25 10:44
"""
from time_tool import TimeTool
import os

class AbstractFileTool:
    """
    将传感器数据写入文件工具
    """
    def __init__(self, file_path='/home/pi/data/', file_ext='txt'):
        self._path = file_path  # 默认文件路径
        self._ext = file_ext   # 文件后缀
        self._file = ''  # 文件对象
        self._date = TimeTool.localtime('%Y-%m-%d-%H:%M')  # 时间
        self._file_name = ''

    def create_file(self, sensor_name, operate='a'):
        self._path = self._path + '/' +sensor_name + '/'  # 设置相应的路径
        if not os.path.exists(self._path):
            os.makedirs(self._path)
        self._file_name = self._path + self._date + '-' + sensor_name + '.' + self._ext  # 路径+文件名+后缀
        try:
            self._file = open(self._file_name, operate)
        except Exception as e:
            print('Failed to open file:' + str(e))
            # quit()

    def write(self, data):
        data = TimeTool.localtime() + data + '\n'  # 数据包装
        if self._file != '':
            self._file.write(data)
        else:
            self.create_file(self._file_name, 'a')
            self._file.write(data)
        self._file.flush()

    def close(self):
        try:
            self._file.close()
        except Exception as e:
            print(str(e))
