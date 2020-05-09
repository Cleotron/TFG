# -*- coding: utf-8 -*-
"""
Created on Tue May  5 13:17:52 2020

@author: ana
"""
import data

import unittest
import random

from solucion1 import get_euclidean, get_distance, get_path

a = data.Base("Base_a", 1, 3, -3)
b = data.Base("Base_b", 2, 4, 4)
c = data.Base("Base_c", 0, -6, -1)

base_list = [a, b, c]


class TestEuclideanDistance(unittest.TestCase):
    def test_distance_ab(self):
        euc = get_euclidean(a, b)
        self.assertEqual(euc, 2**0.5)
        
    def test_distance_bc(self):
        euc = get_euclidean(b, c)
        self.assertEqual(euc, 104**0.5)
        
    def test_distance_ac(self):
        euc = get_euclidean(a, c)
        self.assertEqual(euc, 82**0.5)      
        
        
class TestGetDistance(unittest.TestCase):
    def test_get_distance(self):
        dist = get_distance(base_list)
        self.assertEqual(dist, 2**0.5 + 104**0.5)     
        
        
class TestGetPath(unittest.TestCase):
    def test_get_path(self):    
        path = get_path(base_list)
        self.assertEqual(path, [b, c, a])  
        

if __name__ == '__main__':
    unittest.main()