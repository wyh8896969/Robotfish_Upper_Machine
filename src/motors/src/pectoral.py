#! /usr/bin/env python
# encoding:utf-8
from dynamixel_tools.cpg import CpgPectoral
from dynamixel_tools.xm540 import DxlXM540Motor
from utils.dxl_port import DxlIO
import rospy
from msg.msg import MotionControl

CENTER_POS = 2048

# MODE = ['sync']
class PectoralFin:
    
    def __init__(self):
        """
        胸鳍运动控制节点，接收MotionControl消息，有简单的运动控制，修改消息后还未测试，之前测试成功
        """
        rospy.init_node('pec_fin')
        self._io = DxlIO()
        self._fin_left = DxlXM540Motor(1, self._io)
        self._fin_right = DxlXM540Motor(2, self._io)
        self._sub = rospy.Subscriber('motion_signal',MotionControl, self.get_mode)
        self._mode = 'stop'   # 舵机操作模式
        self._goal_pos = 0   # 舵机目标位置
        self._cpg = CpgPectoral(CENTER_POS).cpg_signal()
        next(self._cpg)  # 启动CPG信号生成器
        
    def get_mode(self, data):
        self._mode = data.motion
        print("mode is set to ", self._mode)

    def setup(self):
        self._fin_left.reverse_center(CENTER_POS)
        self._fin_right.reverse_center(CENTER_POS)

    def run(self):
        while not rospy.is_shutdown():
            while self._mode == 'forward':  # CPG模式摆动
                pos = self._cpg.send((0,0))  # 获取CPG信号元组
                self._mode_sync_sway(pos[0], pos[1])
            while self._mode == 'left':     # 左转 
                self._fin_left.backto_center()
                pos = self._cpg.send((0,0))
                self._fin_right.goto_position(pos[1])
            while self._mode == 'right':      # 右转
                self._fin_right.backto_center()
                pos = self._cpg.send((0,0))
                self._fin_left.goto_position(pos[0])
            if  self._mode == 'dive':      # 下潜
                self._mode_sync_sway(CENTER_POS+512,CENTER_POS-512)
            elif self._mode == 'up':     # 上升
                self._mode_sync_sway(CENTER_POS-512, CENTER_POS+512)
            elif self._mode == 'stop':
                self._mode_sync_sway(CENTER_POS, CENTER_POS)
                
    def _mode_sync_sway(self, pos_left, pos_right):
        """同时摆动到指定位置"""
        self._fin_left.goto_position(pos_left)
        self._fin_right.goto_position(pos_right)

    def close(self):
        self._fin_left.backto_center()
        self._fin_right.backto_center()


if __name__ == "__main__":
    app = PectoralFin()
    app.run()