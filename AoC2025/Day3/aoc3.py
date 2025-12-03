import pandas as pd


df = pd.read_csv('aoc3_input.txt', header=None)
#df = pd.read_csv('aoc3_input_f.txt', header=None)
s = 0
for i in range(len(df[0])):
    line = str(df[0][i])
    mx = 0
    for x in range(len(line)):
        for y in range(x+1, len(line)):
            num = int(line[x] + line[y])
            if mx<num:
                mx = num
    if len(line) == 1:
        mx = line[0]
    print(mx)
    s = s + mx
    
print(s)