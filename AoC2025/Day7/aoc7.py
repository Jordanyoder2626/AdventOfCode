import pandas as pd


with open('aoc7_input.txt','r') as file:
#with open('aoc7_input_f.txt','r') as file:
    all_line = file.readlines()
beams_index = []
cnt = 0
for line in all_line:
    x = line.replace('\n','')
    for i in range(len(x)):
        if x[i] == 'S':
            beams_index.append(i)
        if x[i] == '^' and i in beams_index:
            while i in beams_index:
                beams_index.remove(i)
            beams_index.append(i-1)
            beams_index.append(i+1)
            cnt = cnt+1
        set_beams_index = set(beams_index)
        beams_index = list(set_beams_index)
print(cnt)


