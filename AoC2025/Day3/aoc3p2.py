import pandas as pd


#df = pd.read_csv('aoc3_input.txt', header=None)
df = pd.read_csv('aoc3_input_f.txt', header=None)

sum_nums = 0
for i in range(len(df[0])):
    line = str(df[0][i])
    s = ""
    mx_pos = -1
    for endL in range(12,0,-1):
        mx = 0
        
        for x in range(mx_pos+1,len(line)-endL+1):
            if mx<int(line[x]):
                mx = int(line[x])
                mx_pos = x
        s = s + str(mx)
    sum_nums = sum_nums + int(s)
print(sum_nums)