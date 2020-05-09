# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:16:22 2020

@author: ana
"""

import unittest
import random

import data

from bases_csv import set_demand


class TestSetDemand(unittest.TestCase):
    def setUp(self):
        a = data.Base("Base_a", 1, 3, -3)
        b = data.Base("Base_b", 2, 4, 4)
        c = data.Base("Base_c", 0, -6, -1)        
        self.base_list = [a, b, c]
        
    def test_set_demand(self):
        set_demand(self.base_list)
 
        total = 0
        for i in self.base_list:
            total = total + i.demand
        self.assertEqual(total, 0)
        
    
if __name__ == '__main__':
    unittest.main()
