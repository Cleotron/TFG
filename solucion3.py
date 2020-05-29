# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 16:45:33 2020

@author: ana
""" 

import copy
import math
import random

from bases_csv import get_bases
import data
import solucion1


def get_euclidean(a, b):
    return math.sqrt(pow(a.long - b.long, 2) + pow(a.lat - b.lat, 2))

def get_distance(base_list):
    distance = 0
    
    for x in range (0, len(base_list)-1):
        
        distance = distance + get_euclidean(base_list[x], base_list[x + 1])
    
    return distance


def set_pheromones(phe, original, ants):
    d = get_distance(solucion1.get_path(original))
    init_phe = ants/ d
    for x in original:
        phe[x.name] = {}
        for y in original:
            phe[x.name][y.name] = init_phe

def phe_evaporation(phe, bases, p):
    for x in bases:
        for y in bases:
            phe[x.name][y.name] = phe[x.name][y.name] * (1 - p)


def update_pheromones(phe, visited, deposit):
    for i in range(len(visited) - 1):
        phe[visited[i].name][visited[i + 1].name] = (
            phe[visited[i].name][visited[i + 1].name] + deposit
        )

def choose_from_list(bases, l, n):
    sum = 0
    for i, element in enumerate(l):
        if element != 0:
            sum += element
            if sum >= n:
                return i
    return -1
            
def choose_next(now, bases, phe, truck):
    
    prob_list = []
    sum_prob = 0
    for i, base in enumerate(bases):
        phi = phe[bases[now].name][base.name]
        d = get_euclidean(bases[now], base)
        #if bases[now].name == base.name:
        if d == 0 or base.demand == 0 or (base.demand < 0 and -base.demand > truck):    
            prob = 0
        else:
            prob = phi / (d**2)
            #prob = random.uniform(1000, 10000)
        sum_prob += prob
        prob_list.append(prob)
    n = random.uniform(0.0, sum_prob)    
    return choose_from_list(bases, prob_list, n)

def get_path(original, ants):

    #truck initially empty
    truck = 0;
    
    #best path so far
    best = []
    
    #pheromone in each branch
    #every branch starts with 1 unit 
    phe = {}
    set_pheromones(phe, original, ants)
    
    #choose the best path in 100 iterations
    for _ in range(ants):
        bases = copy.deepcopy(original) 
        visited = []
        
        #first base is chosen at random
        now = random.randint(0, len(bases) - 1)
        
        while any([b.demand < 0 for b in bases]):     
            next = choose_next(now, bases, phe, truck)
    
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
            
        #pheromone evaporation
        phe_evaporation(phe, bases, 0.5)
        
        #update pheromones
        deposit = 1 / (get_distance(visited))
        update_pheromones(phe, visited, deposit)
        
        if (not best) or (get_distance(visited) < get_distance(best)):
            best = visited
        
    return best
 
def main():
    original = get_bases()
    
    #remove stations with demand = 0
    original = [b for b in original if b.demand != 0]

    result = get_path(original, 1000)
    print([o.name for o in result])
    print("total:" , get_distance(result))


if __name__ == "__main__":
    main()

