N = int(input())

sum,st,ed,cnt = 1,1,1,1

while ed != N:
    if sum == N: cnt+=1; ed+=1; sum+=ed
    elif sum > N: sum-=st; st+=1
    else : sum+=ed; ed+=1
print(cnt)