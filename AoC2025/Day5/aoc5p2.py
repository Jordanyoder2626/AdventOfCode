import pandas as pd


#with open('aoc5_input.txt','r') as file:
with open('aoc5_input_f.txt','r') as file:
    all_line = file.readlines()
nex = False
ranges = []
testing = []
for line in all_line:
    x = line.replace('\n','')
    if len(x) != 0:
        if nex:
            testing.append(int(x))
        else:
            ranges.append(x)
    else:
        nex = True
fresh = []
tupes = []
for rng in ranges:
    splt = rng.split('-')
    low = int(splt[0])
    high = int(splt[1])
    tupes.append((low,high))

tupes.sort(key = lambda x:x[0])

for tupe in tupes:
    if len(fresh) == 0:
        fresh.append(tupe)
    if fresh[len(fresh)-1][1]< tupe[0]:
        fresh.append(tupe)
    if fresh[len(fresh)-1][1]>= tupe[0]:
        fresh[len(fresh)-1] = (fresh[len(fresh)-1][0]), max(fresh[len(fresh)-1][1], tupe[1])

tot = 0
for tupel in fresh:
    tot = tot+1 + tupel[1]- tupel[0]
print(tot)