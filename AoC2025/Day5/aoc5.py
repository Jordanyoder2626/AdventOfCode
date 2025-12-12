import pandas as pd


with open('aoc5_input.txt','r') as file:
#with open('aoc5_input_f.txt','r') as file:
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
cnt=0
for num in testing:
    fresh = False
    for rng in ranges:
        splt = rng.split('-')
        low = int(splt[0])
        high = int(splt[1])
        if num >=low and num<=high:
            fresh = True
    if fresh:
        cnt = cnt+1
print(cnt)
    

