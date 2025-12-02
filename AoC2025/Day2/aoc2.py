import pandas as pd

i = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
#i = "11-22"
spl = i.split(',')
id_sum = 0
for rng in spl:
    s = rng.split('-')
    if len(s) == 2:
        low = s[0]
        high = s[1]
        # print("low" + low)
        # print("high" + high)
        for num in range(int(low),int(high)+1):
            str_num = str(num)
            if len(str_num)%2 == 0:
                mid = len(str_num)/2
                first = str_num[:int(mid)]
                last = str_num[int(mid): len(str_num)]
                if first==last:
                    id_sum = id_sum + num



    else:
        id_sum = id_sum+0

print(id_sum)