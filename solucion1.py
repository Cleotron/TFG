# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:00:16 2020

@author: ana
"""
import math

from bases_csv import load_data
import data


def get_euclidean(a, b):
    return math.sqrt(pow(a.long - b.long, 2) + pow(a.lat - b.lat, 2))

def get_distance(base_list):
    distance = 0
    
    for x in range (0, len(base_list)-1):
        
        distance = distance + get_euclidean(base_list[x], base_list[x + 1])
    
    return distance

def get_path(bases):
    best = []
    for _ in range(100):
        ordered = sorted(bases, key=lambda Base: Base.demand, reverse=True)
        if (not best) or get_distance(ordered) < get_distance(best):
            best = ordered
        
    return best

def main():
    original = load_data('C:\\Users\\ana\\Nextcloud\\UOC\\PECS2020\\codigoTFG\\Bicimad0618.csv')
    
    #remove stations with demand = 0
    original = [b for b in original if b.demand != 0]

    result = get_path(original)
    print([o.name for o in result])
    print("total:" , get_distance(result))


if __name__ == "__main__":
    main()
