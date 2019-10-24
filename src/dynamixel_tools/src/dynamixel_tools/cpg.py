#! /usr/bin/env python
# encoding:utf-8


class CpgPectoral:
    def __init__(self, center):
        self._fish_pec_speed = 8
        self._step = 1
        self.P = 60
        self.y2 = 0.2
        self.x2 = 0.2
        self._center = center
        self.k_y2 = 5.0
        self._pos_per_degree = 11.38
        self.h = 0.01
        
    def _cpg_generator(self):
        while True:
            omega = 14.0 + self._fish_pec_speed * self._step
            x2r = -omega * self.y2 + self.x2 * (self.P - self.x2 ** 2 - self.y2 ** 2)
            y2r = omega * self.x2 + self.y2 * (self.P - self.x2 ** 2 - self.y2 ** 2)
            self.x2 += self.h * x2r
            self.y2 += self.h * y2r
            pec_cpg_data0 = (self._center + self.k_y2 * self.y2 * self._pos_per_degree)
            pec_cpg_data1 = (self._center - self.k_y2 * self.y2 * self._pos_per_degree)
            yield pec_cpg_data0, pec_cpg_data1
            
    def cpg_signal(self):
        #while True:
            #yield self._cpg_generator()
        while True:
            omega = 14.0 + self._fish_pec_speed * self._step
            x2r = -omega * self.y2 + self.x2 * (self.P - self.x2 ** 2 - self.y2 ** 2)
            y2r = omega * self.x2 + self.y2 * (self.P - self.x2 ** 2 - self.y2 ** 2)
            self.x2 += self.h * x2r
            self.y2 += self.h * y2r
            pec_cpg_data0 = (self._center + self.k_y2 * self.y2 * self._pos_per_degree)
            pec_cpg_data1 = (self._center - self.k_y2 * self.y2 * self._pos_per_degree)
            yield pec_cpg_data0, pec_cpg_data1