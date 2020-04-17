# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 19:31:09 2020

@author: ana
"""
import dataclasses
import math
import random
#import pdb; pdb.set_trace()

def get_euclidean(a, b):
    return math.sqrt(pow(a.long - b.long, 2) + pow(a.lat - b.lat, 2))

def get_distance(base_list):
    distance = 0
    
    for x in range (0, len(base_list)-1):
        
        distance = distance + get_euclidean(base_list[x], base_list[x + 1])
    
    return distance

#estaciones
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

original = [p1, p2, p3, p4, p5] 

#camion inicialmente sin bicis
truck = 0;

#lista de mejor camino hasta ahora
best = []

#ir a una estacion aleatoria - si demand = 0 eliminar de la lista
#coger/dejar bicis
#repetir hasta lista vacía

original = [b for b in original if b.demand != 0]

#bucle con 20 repeticiones y quedarse con la mejor
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
    print("----")    
    print("visited:", [o.name for o in visited])
    print("distance visited:" , get_distance(visited)) 
    
    if (not best) or (get_distance(visited) < get_distance(best)):
        best = visited

 
print("----")    
print("best:", [o.name for o in best])  
print("total:" , get_distance(best))   



