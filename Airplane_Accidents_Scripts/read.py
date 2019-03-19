import pandas as pd
import csv
import bisect

#if __name__=="__main__":
f=open('AviationData.txt')
aviation_data=f.readlines()
aviation_list=[]
for line in aviation_data:
    temp=line.split(' | ')
    for word in temp:
        aviation_list.append(word.strip())
        
srtd_aviation=sorted(aviation_list)

#log(n) time
lax_idx=bisect.bisect_left(srtd_aviation,'LAX94LA336')
print(srtd_aviation[lax_idx], lax_idx)

#linear time
for idx, word in enumerate(srtd_aviation):
    if 'LAX94LA336' in word:
        print('Found at index:', idx)
        
#Tradeoffs of linear vs log time algorithms
#Linear algorithm is easier to write, unless a function is
#is used.
      

