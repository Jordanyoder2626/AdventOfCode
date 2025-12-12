import pandas as pd


#with open('aoc6_input.txt','r') as file:
with open('aoc6_input_f.txt','r') as file:
    all_line = file.readlines()

df = pd.DataFrame(columns = list(range(0, 1000)))
vals = []
#print("df len" + str(len(df)))
for line in all_line:
    line = line.replace('\n','')
    x = line.replace('     ',' ')
    x = line.replace('    ',' ')
    x = x.replace('   ',' ')
    x = x.replace('  ',' ')
    x = x.replace(' ',',')
    if x[0] == ',':
       x = x[1:]
    if x[len(x)-1] == ',':
       x = x[:len(x)-1]
    #print(len(x.split(',')))
    if x[0] not in ['+','*']:
        nums = x.split(',')
        df.loc[len(df)] = nums
        df = df.astype('int64')
    else:
        ops = x.split(',')
        for i in range(len(df.columns)):
            
            #print(ops[i])
            if ops[i] == '+':
                vals.append(int(df[i].sum()))
            else:
                mult = 1
                for num in df[i]:
                    mult = mult*int(num)
                vals.append(mult)


print(sum(vals))
