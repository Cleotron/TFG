# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:27:34 2020

@author: ana
"""

import unittest
import random

import data

from solucion3 import get_euclidean, get_distance, get_path, set_pheromones, choose_from_list, choose_next, phe_evaporation, update_pheromones

a = data.Base("Base_a", 1, 3, -3)
b = data.Base("Base_b", 2, 4, 4)
c = data.Base("Base_c", 0, -6, -1)

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
        path = get_path(base_list, 5)
        self.assertEqual(path[0].name, "Base_b")
        self.assertEqual(path[1].name, "Base_a")
        self.assertEqual(path[2].name, "Base_c")

class TestChooseFromList(unittest.TestCase):
    def test_choose_from_list(self):
        choose = choose_from_list(base_list, [1.5, 6.1, 2, 4], 0)
        self.assertEqual(choose, 0) 

class TestChooseNext(unittest.TestCase):
    def setUp(self):
        self.phe = {'Base_a': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1},
                    'Base_b': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1},
                    'Base_c': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1}}
    def test_choose_next(self):
        next = choose_next(1, base_list, self.phe, 5)
        self.assertTrue(0 <= next < len(base_list))
        
class TestPheEvaporation(unittest.TestCase):
    def setUp(self):
        self.phe = {'Base_a': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1},
                    'Base_b': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1},
                    'Base_c': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1}}
    def test_phe_evaporation_a(self):
        phe_evaporation(self.phe, base_list, 0.5)
        self.assertEqual(self.phe, 
                    {'Base_a': {'Base_a': 0.5, 'Base_b': 0.5, 'Base_c': 0.5},
                    'Base_b': {'Base_a': 0.5, 'Base_b': 0.5, 'Base_c': 0.5},
                    'Base_c': {'Base_a': 0.5, 'Base_b': 0.5, 'Base_c': 0.5}})
    def test_phe_evaporation_b(self):
        phe_evaporation(self.phe, base_list, 0.4)
        self.assertEqual(self.phe, 
                    {'Base_a': {'Base_a': 0.6, 'Base_b': 0.6, 'Base_c': 0.6},
                    'Base_b': {'Base_a': 0.6, 'Base_b': 0.6, 'Base_c': 0.6},
                    'Base_c': {'Base_a': 0.6, 'Base_b': 0.6, 'Base_c': 0.6}})
        
class TestUpdatePheromones(unittest.TestCase):
    def setUp(self):
        self.phe = {'Base_a': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1},
                    'Base_b': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1},
                    'Base_c': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1}}
        self.visited = [a, b]
    def test_update_pheromones(self):
        update_pheromones(self.phe, self.visited, 2)
        self.assertEqual(self.phe, 
                    {'Base_a': {'Base_a': 1, 'Base_b': 3, 'Base_c': 1},
                     'Base_b': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1},
                     'Base_c': {'Base_a': 1, 'Base_b': 1, 'Base_c': 1}})
        




if __name__ == '__main__':
    unittest.main()
