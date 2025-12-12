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
# paired = []
# cnt = 0

for i in range(len(tupes)):
    for j in range(i+1, len(tupes)):
        dist = euclidean(tupes[i], tupes[j])
        circ.append((dist,i,j))
    
circ.sort(key = lambda x:x[0])    
#circ = circ[0:1000]

circuits = []
cnt = 0
for c in circ:
    c1 = c[1]
    c2 = c[2]
    newC = True
    for i in range(len(circuits)):
        #print (circuits)
        temp = circuits[i]
        if c1 in temp and c2 not in temp:
            ad = [c2]
            for x in range(i, len(circuits)):
                if c2 in circuits[x]:
                    ad = circuits.pop(x)
                    break
            
            temp = temp + ad
            newC = False
            circuits[i] = temp
            cnt = cnt+1
            break
        if c2 in temp and c1 not in temp:
            ad = [c1]
            for x in range(i, len(circuits)):
                if c1 in circuits[x]:
                    ad = circuits.pop(x)
                    break

            temp = temp + ad
            newC = False
            circuits[i] = temp
            cnt = cnt+1
            break
        if c1 in temp and c2 in temp:
            newC = False
            cnt= cnt+1
            break
    if newC:
        circuits.append([c1,c2])
        cnt = cnt+1
    if cnt == 1000:
        break
#print(circuits)
mx = 1
for z in range(3):
    #print(circ)
    max_len = 0
    max_circ = 0
    for idx in range(len(circuits)):
        cir = len(circuits[idx])
        if max_len<cir:
            max_circ = idx
            max_len = cir
    circuits.pop(max_circ)
    mx = mx*max_len




print(mx)
