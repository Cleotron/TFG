# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:27:34 2020

@author: ana
"""

import unittest
import random

from solucion3 import Base, get_euclidean, get_distance, get_path, set_pheromones

a = Base("Base_a", 1, 3, -3)
b = Base("Base_b", 2, 4, 4)
c = Base("Base_c", 0, -6, -1)

base_list = [a, b, c]

phe = {}


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
        random.seed(1)
        path = get_path(base_list)
        self.assertEqual(path, [c, a, b]) 
        
class TestSetPheromones(unittest.TestCase):
    def test_set_pheromones(self):
        phe_list = set_pheromones(phe, base_list)
        self.assertEqual(phe, {'Base_a': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1},
                               'Base_b': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1},
                               'Base_c': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1}})
        

if __name__ == '__main__':
    unittest.main()
