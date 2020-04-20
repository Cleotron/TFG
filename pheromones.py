# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:45:33 2020

@author: ana
""" 

import dataclasses
import math
import random

def get_euclidean(a, b):
    return math.sqrt(pow(a.long - b.long, 2) + pow(a.lat - b.lat, 2))

def get_distance(base_list):
    distance = 0
    
    for x in range (0, len(base_list)-1):
        
        distance = distance + get_euclidean(base_list[x], base_list[x + 1])
    
    return distance

@dataclasses.dataclass
class Base:
    name: str
    long: float
    lat: float
    demand: int
    

p1 = Base("Agustín de Betancourt", -3.6956047, 40.4440297, -4)
p2 = Base("Alberto Alcocer", -3.684715,40.4585318, 4)
p3 = Base("Alcalá", -3.6801307, 40.4226906, -3)
p4 = Base("Alcántara", -3.6738714, 40.4261851, 4)
p5 = Base("Almadén", -3.693225, 40.4108472,-1)

#list of all the stations
original = [p1, p2, p3, p4, p5] 

#remove stations with demand = 0
original = [b for b in original if b.demand != 0]

#truck initially empty
truck = 0;

#best path so far
best = []

#pheromone in each branch
#every branch starts with 1 unit 
phe = {}

for x in original:
    phe[x.name] = {}
    for y in original:
        phe[x.name][y.name] = 1

#choose the best path in 100 iterations
for _ in range(100):
    bases = original.copy() 
    visited = []
    
    #first base is chosen at random
    now = random.randint(0, len(bases) - 1)
    
    while len(bases) > len(visited):     
        #create a weighed list of bases: each base will appear once per pheromon
        #unit
        weighed = []
        for i, base in enumerate(bases):
            if base not in visited:
                pherom = phe[bases[now].name][base.name]
                for _ in range(pherom):
                    weighed.append(i)
                    
        #next base is chosen from the weighed list of bases
        next = random.choice(weighed)
        
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
 
    print("visited:", [o.name for o in visited])
    print("distance visited:" , get_distance(visited)) 
    print()
    
    if (not best) or (get_distance(visited) < get_distance(best)):
        best = visited

 
print("----")    
print("best:", [o.name for o in best])  
print("total:" , get_distance(best))   


