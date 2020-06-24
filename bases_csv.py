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
    
def write_csv(base_list):
    with open('C:\\Users\\ana\\Nextcloud\\UOC\\PECS2020\\codigoTFG\\Bases.csv', 'w', newline='', encoding='utf-8') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for base in base_list:
            wr.writerow([base.name, base.long, base.lat, base.demand])

def get_bases():
    bases = []
    with open('C:\\Users\\ana\\Nextcloud\\UOC\\PECS2020\\codigoTFG\\Bases.csv', encoding='utf-8') as csvfile:
        basereader = csv.reader(csvfile, delimiter=',')
        basereader.__next__()
        for row in basereader:
            bases.append(data.Base(row[0], float(row[1]), float(row[2]), float(row[3])))
    return bases    

def main():
    bases = load_data('Bicimad0618.csv')
    write_csv(bases)
    
if __name__ == "__main__":
    main()


    


