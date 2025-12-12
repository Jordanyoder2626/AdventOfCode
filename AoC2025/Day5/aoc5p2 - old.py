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
for rng in ranges:
    splt = rng.split('-')
    low = int(splt[0])
    high = int(splt[1])
    if len(fresh) == 0:
        fresh.append((low,high))
    for tupe in range(len(fresh)):
        bot = fresh[tupe][0]
        top = fresh[tupe][1]
        if high<bot:
            fresh.insert(tupe,(low,high))
            break
        elif low>bot and low<=top:
            fresh[tupe] = (bot,max(top, high))
            for swol in range(tupe+1, len(fresh)):
                b = fresh[swol][0]
                t = fresh[swol][1]
                if high>t:
                    del fresh[swol]
                    break
                elif high>b and high<=t:
                    fresh[swol] = (high+1,t)
            break
        elif high<top and high>=bot:
            fresh[tupe] = (min(low,bot),top)
            break
        elif low>top and tupe == len(fresh)-1:
            fresh.append((low,high))
tot = 0
for tupel in fresh:
    tot = tot+1 + tupel[1]- tupel[0]
print(tot)
    
