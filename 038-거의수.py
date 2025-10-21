import math

min,max = map(int, input().split())
a = [0]*10000001

for i in range(2,len(a)):
    a[i] = i;
    
for i in range(int(math.sqrt(len(a)+1))):
    if a[i] == 0: continue
    
    for j in range(i+i,len(a), i):
        a[j]=0
        
res = 0
for i in range(2,len(a)):
    if a[i] != 0:
        tmp = a[i]
        while a[i] <= max/tmp:
            if a[i] >= min/tmp:
                res+=1
            tmp *= a[i]
print(res)