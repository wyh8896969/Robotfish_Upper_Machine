# encoding: utf-8
import time

class TimeTool:
    """
    自定义日期工具
    """
    @staticmethod
    def time():
        return time.time()

    @staticmethod
    def localtime(fmt='%Y-%m-%d-%H:%M:%S '):
        fmt = fmt
        localtime = time.strftime(fmt, time.localtime(time.time()))
        return localtime