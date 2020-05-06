# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:00:16 2020

@author: ana
"""
import dataclasses
import math



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

bases = [p1, p2, p3, p4, p5] 

def get_euclidean(a, b):
    return math.sqrt(pow(a.long - b.long, 2) + pow(a.lat - b.lat, 2))

def get_distance(base_list):
    distance = 0
    
    for x in range (0, len(base_list)-1):
        
        distance = distance + get_euclidean(base_list[x], base_list[x + 1])
    
    return distance

def get_path(bases):
    ordered = sorted(bases, key=lambda Base: Base.demand, reverse=True)
    
    return ordered

def main():
    result = get_path(bases)
    print([o.name for o in result])
    print("total:" , get_distance(result))


if __name__ == "__main__":
    main()
