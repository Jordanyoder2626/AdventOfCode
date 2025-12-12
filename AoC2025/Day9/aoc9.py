import pandas as pd


#with open('aoc9_input.txt','r') as file:
with open('aoc9_input_f.txt','r') as file:
    all_line = file.readlines()
tupes = []
for line in all_line:
    line = line.replace('\n','')
    spl = line.split(',')
    x = int(spl[0])
    y = int(spl[1])
    tupes.append((x,y))
tupes = sorted(tupes, key=lambda x: x[0], reverse=False)
# print(tupes[0])
# print(tupes[1])
areas = []
for i in range(len(tupes)):
    area = 0
    for j in range(i+1, len(tupes)):
        t1 = tupes[i]
        t2 = tupes[j]

        x1 = t1[0]
        y1 = t1[1]
        x2 = t2[0]
        y2 = t2[1]

        area = (max(x1,x2) - min(x1,x2) + 1) * (max(y1,y2) - min(y1,y2)+1)
        areas.append((area,i,j))
areas = sorted(areas, key=lambda x: x[0], reverse=True)
for a in areas:
    t1 = tupes[a[1]]
    t2 = tupes[a[2]]
    x1 = int(min(t1[0],t2[0])) #2
    x2 = int(max(t1[0],t2[0])) #9
    y1 = int(min(t1[1],t2[1])) #3
    y2 = int(max(t1[1],t2[1])) #5
  

    confirm1 = 0
    confirm2 = 0
    confirm3 = 0
    confirm4 = 0
    for tr in range(len(tupes)):
        t = tupes[tr]
        tx = int(t[0])
        ty = int(t[1])
        # print(str(tx) + "," + str(ty))
        # print(str(x1) + "," + str(y2))
        # print()
        #checking top left x1,y1 2,3 theres 2,3
        if tx<=x1 and ty<=y1:
            confirm1 = 1
            # print(str(tx) + "," + str(ty))
            # print(str(x1) + "," + str(y1))
            # print()
            #print(t)
        #checking top right x2,y1 2,9 theres 11,1
        if tx>=x2 and ty<=y1:
            confirm2 = 1
           # print(t)
        #checking bottom left x1,y2 2,5 theres 2,5
        if tx<=x1 and ty>=y2:
            confirm3 = 1
            # print(str(tx) + "," + str(ty))
            # print(str(x1) + "," + str(y2))
            # print()
        #checking bottom right x2,y2 9,5 theres 11,7
        if tx>=x2 and ty>=y2:
            confirm4 = 1
        
    if confirm4 == 1 and confirm2 == 1 and confirm3 == 1 and confirm1 == 1:
        print(a)
        break
#print(tupes)

    
    













