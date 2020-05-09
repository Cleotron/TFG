# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:14:57 2020

@author: ana
"""

import csv
import dataclasses
import random

import data

def set_demand(original):
    for _ in range(4080):
        current_base = random.randint(0, len(original) - 1)
        original[current_base].demand = original[current_base].demand - 1
        current_base = random.randint(0, len(original) - 1)
        original[current_base].demand = original[current_base].demand + 1


def load_data(path):
    original = []
    
    #open bicimad dataset and set all demands to 0
    with open(path, encoding='utf-8') as csvfile:
        basereader = csv.reader(csvfile, delimiter='\t')
        basereader.__next__()
        for row in basereader:
            original.append(data.Base(row[0], float(row[1]), float(row[2]), 0))
        
    
    #set demands randomly with net sum 0
    set_demand(original)
    
    return original





    


