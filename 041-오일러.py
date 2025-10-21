import math
n= int(input())
res = n

for i in range(2, int(math.sqrt(n))+1): #제곱근까지만
    if n % i == 0:                      #i가 소인수 인지확인
        result -= res / i               # 결괏값업뎃
        while n % i == 0:               #?
            n /= i

if n>1:
    res -= res/n
    
print(int(res))            