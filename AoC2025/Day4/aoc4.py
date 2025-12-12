import pandas as pd


#df = pd.read_csv('aoc4_input.txt', header=None)
df = pd.read_csv('aoc4_input_f.txt', header=None)
cnt = 0
for i in range(len(df[0])):
    line = df[0][i]
    #print(line)
    for j in range(len(line)):
        char = line[j]
        #checking for rolls
        if char == '@':
            #if a roll look at the 3x3 grid around it
            rolls = -1 #accounting for the roll in i,j
            for x in range(max(i-1,0), min(i+2, len(df[0]))):
                lne = df[0][x]
                #trips = ""

                for y in range(max(j-1,0), min(j+2, len(lne))):
                    #trips = trips + lne[y]
                    if lne[y] == '@':
                        rolls = rolls +1
                #print(trips)
            if rolls<4:
                cnt = cnt+1
    
print(cnt)

