import pandas as pd
from scipy.spatial.distance import euclidean

#with open('aoc8_input.txt','r') as file:
with open('aoc8_input_f.txt','r') as file:
    all_line = file.readlines()
tupes = []
for line in all_line:
    line = line.replace('\n','')
    spl = line.split(',')
    x = int(spl[0])
    y = int(spl[1])
    z = int(spl[2])
    tupes.append((x,y,z))
circ = []
paired = []
cnt = 0
while cnt<1000:
    minD = 2147483647
    pair = (0,0)
    for i in range(len(tupes)):
        for j in range(i+1, len(tupes)):
            dist = euclidean(tupes[i], tupes[j])
            if dist < minD and (i,j) not in paired:
                minD = dist
                pair = i,j
    
    
    
    
    newC = True
    for x in range(len(circ)):
        temp = circ[x]
        if pair[0] in temp and pair[1] not in temp:
            temp.append(pair[1])
            cnt = cnt+1
            circ[x] = temp
            newC = False
            break
        if pair[1] in temp and pair[0] not in temp:
            temp.append(pair[0])
            cnt = cnt+1
            circ[x] = temp
            newC = False
            break
        if pair[1] in temp and pair[0] in temp:
            newC = False
            cnt = cnt+1
            break
    if newC:
        cnt = cnt+1
        circ.append([pair[0],pair[1]])
    paired.append(pair)
    print(cnt)

mx = 1
for z in range(3):
    #print(circ)
    max_len = 0
    max_circ = 0
    for idx in range(len(circ)):
        cir = len(circ[idx])
        if max_len<cir:
            max_circ = idx
            max_len = cir
    circ.pop(max_circ)
    mx = mx*max_len




print(mx)
