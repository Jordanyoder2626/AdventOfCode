import pandas as pd


#with open('aoc6_input.txt','r') as file:
with open('aoc6_input_f.txt','r') as file:
    all_line = file.readlines()



skip = 0
vals = []
nums = []
for x in range(len(all_line[0])-1):
    if skip == 0:
        
        st = ""
        op = ""
        for line in all_line:
            line = line.replace('\n','')
            line = line[::-1]
            #print(len(line))
            if line[x] in ['+','*']:
                #vals.append(int(st))
                op = line[x]
                skip = 1
                
            else:
                st = st + line[x]
        #vals.append(int(st))
        if skip == 1:
            vals.append(int(st))
            print(vals)
            num = 0
            if op == '+':
                nums.append(int(sum(vals)))
            else:
                mult = 1
                for num in vals:
                    mult = mult*int(num)
                nums.append(mult)

            vals = []

        else:
            vals.append(int(st))
    else:
        skip = 0
print(sum(nums))

