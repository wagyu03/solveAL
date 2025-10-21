def gcd(a,b):
    if b == 0: return a
    else : return gcd(b,a%b)
    
a, b = map(int, input().split())
res = gcd(a,b)

for i in range(res):
    print(1,end="")
    
    