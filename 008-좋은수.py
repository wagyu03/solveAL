n = int(input() )
a = list(map(int, input().split()))
cnt = 0
for k in a:
    find,i,j = k,0,n-1
    
    while i<j:
        if a[i]+a[j]== find:
            if i != k and j != k:
                cnt+=1
                break
            elif i == k:
                i+=1
            elif j== k:
                j-=1
        elif a[i]+a[j] < find : i+=1
        else : j-=1
print(cnt)   