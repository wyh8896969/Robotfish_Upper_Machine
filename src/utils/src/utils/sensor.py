# encoding: utf-8
"""
@version: 1.0
@author: 
@file: sensors
@time: 2019/7/25 15:02
"""
from file_tool import AbstractFileTool


class SensorBase:
    def __init__(self, io, name):
        """
        传感器的基类，完成传感器通用底层操作，定义通用接口
        
        Parameters
        ----------
        io : [type]
            当前可不使用
        name : [type]
            传感器名，用于查找文件存储路径、统一控制
        """
        self._io = io
        self.name = name
        self._file_tool = AbstractFileTool()
        self.setup()

    def setup(self):
        self._file_tool.create_file(self.name)
        self.init()

    def init(self):
        """传感器初始化"""
        pass

    def read_data(self):
        """返回传感器读取的数据"""
        pass

    def write_to_file(self, data):
        """
        写入文件，子类直接调用即可
        
        Parameters
        ----------
        data : str
            待写入的数据
        """
        self._file_tool.write(data)

    def close(self):
        """关闭文件"""
        self._file_tool.close()