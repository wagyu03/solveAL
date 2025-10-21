n = int(input())
a = list(map(int, input().split()))
ans = [0]*n
S = []

for i in range(n):
    while S and a[S[-1]] < a[i]:
        ans[S.pop()] = a[i]
    S.append(i)

while S:
    ans[S.pop()] = -1
    
result = ""

for i in range(n):
    result += str(ans[i])+" "
print(result)
        
    
    
