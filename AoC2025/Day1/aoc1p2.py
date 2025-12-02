import pandas as pd


#df = pd.read_csv('aoc1_input.txt', header=None)
df = pd.read_csv('aoc1_input_f.txt', header=None)
point = 50
count = 0
for i in range(len(df[0])):
    rot = df[0][i]
    if rot[:1] == 'L':
        oldP = point
        rot = int(rot[1:])
        count = int(count + rot//100)
        point = point - rot%100
        if point < 0 and abs(point)%100 !=0:
            count = count+1
            point = (point%100)
            if oldP == 0:
                count = count-1
            
        if abs(point)%100 == 0:
            count = count+1
            point = 0
            #count = count+1
        
        print("Point after L: " + str(point))
        print("count after L: " + str(count))
    else:
        oldP = point
        rot = int(rot[1:])
        count = int(count + rot//100)
        point = point + rot%100
        if point > 100 and abs(point)%100 !=0:
            count = count+1
            point = point % 100
            if oldP == 0:
                count = count-1
        if point % 100==0:
            count = count+1
            point = 0
            #count = count+1
        
        print("Point after R: " + str(point))
        print("count after R: " + str(count))
print(count)