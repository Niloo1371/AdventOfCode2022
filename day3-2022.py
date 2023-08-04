from aocd import get_data
import numpy as np
import string

letters = []

file = get_data(day=3, year=2022)
lines = file.strip().split('\n')
for line in lines:
    comp1 = line[:int(len(line)/2)]
    comp2 = line[int(len(line)/2):]
    l = ''.join(set(comp1).intersection(comp2))
    letters.append(l)

lowercase = {}
for i,j in enumerate(string.ascii_lowercase): 
    lowercase[j] = np.linspace(1,26,26)[i]

uppercase = {}
for i,j in enumerate(string.ascii_uppercase): 
    uppercase[j] = np.linspace(27,52,26)[i]

all = {**lowercase, **uppercase}
pr = sum([all[i] for i in letters])
