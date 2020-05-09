# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:31:09 2020

@author: ana
"""
import math
import random

import data


def get_euclidean(a, b):
    return math.sqrt(pow(a.long - b.long, 2) + pow(a.lat - b.lat, 2))

def get_distance(base_list):
    distance = 0
    
    for x in range (0, len(base_list)-1):
        
        distance = distance + get_euclidean(base_list[x], base_list[x + 1])
    
    return distance


#choose the best path in 100 iterations
def get_path(original):
    #truck initially empty
    truck = 0;
    
    #best path so far
    best = []

    for _ in range(100):
        bases = original.copy() 
        visited = []
        
        while (len(bases) > 0):
        
            x = random.randrange(len(bases))
            
            visited.append(bases[x])
            
            if bases[x].demand > 0:
                truck = truck + bases[x].demand
                bases[x].demand = 0
               
            
            if bases[x].demand < 0:
                if abs(bases[x].demand) > truck:
                    bases[x].demand = bases[x].demand + truck
                    truck = 0
                else:
                    truck = bases[x].demand + truck
                    bases[x].demand = 0
                    
            if bases[x].demand == 0:
                bases.remove(bases[x])
    
        if (not best) or (get_distance(visited) < get_distance(best)):
            best = visited
 
    return best

def main():
    p1 = data.Base("Agustín de Betancourt", -3.6956047, 40.4440297, -4)
    p2 = data.Base("Alberto Alcocer", -3.684715,40.4585318, 4)
    p3 = data.Base("Alcalá", -3.6801307, 40.4226906, -3)
    p4 = data.Base("Alcántara", -3.6738714, 40.4261851, 4)
    p5 = data.Base("Almadén", -3.693225, 40.4108472,-1)
    
    #list of all the stations
    original = [p1, p2, p3, p4, p5] 
    
    #remove stations with demand = 0
    original = [b for b in original if b.demand != 0]
    result = get_path(original)
    print([o.name for o in result])
    print("total:" , get_distance(result))


if __name__ == "__main__":
    main()