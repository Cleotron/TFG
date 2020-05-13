# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:45:33 2020

@author: ana
""" 

import copy
import math
import random

from bases_csv import load_data
import data


def get_euclidean(a, b):
    return math.sqrt(pow(a.long - b.long, 2) + pow(a.lat - b.lat, 2))

def get_distance(base_list):
    distance = 0
    
    for x in range (0, len(base_list)-1):
        
        distance = distance + get_euclidean(base_list[x], base_list[x + 1])
    
    return distance


def set_pheromones(phe, original):
    for x in original:
        phe[x.name] = {}
        for y in original:
            phe[x.name][y.name] = 1
            
            
def choose_next(now, bases, visited, phe):
    weighed = []
    for i, base in enumerate(bases):
        if base not in visited:
            pherom = phe[bases[now].name][base.name]
            for _ in range(pherom):
                weighed.append(i)   
    return random.choice(weighed) 

def get_path(original):

    #truck initially empty
    truck = 0;
    
    #best path so far
    best = []
    
    #pheromone in each branch
    #every branch starts with 1 unit 
    phe = {}
    set_pheromones(phe, original)
    
    #choose the best path in 100 iterations
    for _ in range(50):
        bases = copy.deepcopy(original) 
        visited = []
        
        #first base is chosen at random
        now = random.randint(0, len(bases) - 1)
        
        while len(bases) > len(visited):     
            next = choose_next(now, bases, visited, phe)
            
            #update pheromones
            phe[bases[now].name][bases[next].name] += 1  
    
            if bases[next].demand > 0:
                truck = truck + bases[next].demand
                bases[next].demand = 0
               
            
            if bases[next].demand < 0:
                if abs(bases[next].demand) > truck:
                    bases[next].demand = bases[next].demand + truck
                    truck = 0
                else:
                    truck = bases[next].demand + truck
                    bases[next].demand = 0
    
    
            now = next
            
            #update visited
            visited.append(bases[next])
        
        if (not best) or (get_distance(visited) < get_distance(best)):
            best = visited
        
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

