import pandas as pd


#with open('aoc7_input.txt','r') as file:
with open('aoc7_input_f.txt','r') as file:
    all_line = file.readlines()
x = all_line[0].replace('\n','')
beams_index = list(range(0, len(x)))
zero = [0 for i in range(len(x))]
df = pd.DataFrame([beams_index,zero,zero])
cnt = 0
for line in all_line:
    x = line.replace('\n','')
    for i in range(len(x)):
        if x[i] == 'S':
            df[i][1] = 1
            df[i][2] = 1
        if x[i] == '^' and df[i][2] == 1:
            df[i][2] = 0
            new_weight = df[i][1]
            df[i][1]=0

            #adding left
            df[i-1][2] =1
            df[i-1][1] = new_weight + df[i-1][1]

            #adding right
            df[i+1][2] =1
            df[i+1][1] = new_weight + df[i+1][1]

            
        # set_beams_index = set(beams_index)
        # beams_index = list(set_beams_index)
    #cnt = cnt+len(beams_index)
print(df.loc[1].sum())


