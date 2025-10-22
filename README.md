# solveAL
문제 해결 기법 백준코드와 풀이
004. { 구간합 구하기2 } : 31p

> 1차원 배열
```
베열 채우기 > S[i]  = s[i-1] + a[i]
값 구하기 : s[j] - s[i-1]
```
> 2차원 배열
```
채우기 : D[ i ][ j ] = D[ i ][  j-1 ] + D[ i-1 ][ j ] - D[ i-1][ j-1 ] + A[ i ][ j ] 
구하기 : D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
```
-------------------------------------------------------------------------------------------

006. { 연속된 자연수의 합 구하기 }: 40p

> st, ed 값을 이용해 둘의 합이 N보다 크면 <mark>st++</mark> 하고, 작으면 <mark>ed++</mark>
```
N = int(input())

sum,st,ed,cnt = 1,1,1,1	

while ed != N:
    if sum == N: cnt+=1; ed+=1; sum+=ed # 수 일치시 카운트 증가
    elif sum > N: sum-=st; st+=1 #합이 N보다 커서 st를 증가
    else : sum+=ed; ed+=1	#합이 N보다 작으니 ed를 증가
print(cnt)
```
-------------------------------------------------------------------------------------------

008. { 좋은수 구하기 }: 47p

> 투포인터 i,j를 시작과 끝으로 설정, 천천히 좁히면서, 
> 기준값 k (배열의 순서대로 값)과 동일할때까지 i+j를 함,
> 겹치면 i,j 수를 변경

```
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
```
-------------------------------------------------------------------------------------------

012. { 오큰수 구하기 } 68p

> 스택에 인덱스값을 넣고, 인덱스 값을 활용해 다음 들어오는 수열값이 더크면
> 인덱스를 팝을 하여 저장배열에 넣는다.
```
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
```

-------------------------------------------------------------------------------------------
++ { 버블정렬 }

```
for i in range(n-1):
	for j in range(n-1-i):
		if n[i] > n[i+1]:
			tmp = n[i]
			n[i] = n[j]
			n[j] = tmp
```

-------------------------------------------------------------------------------------------

019. { K번째 수 구하기 } 101p

> 퀵정렬과 이분탐색을 통하여
원하는 K까지만 빠르게 도달

```
n , m = map(int,input().split())
a = list(map(int, input().split()))

def quickSort(s,e,k):
    global a
    if s<e:
        pivot = partition(s,e)
        
        if pivot == k: return
        elif k < pivot: quickSort(s,pivot-1,k)
        else: quickSort(pivot+1,e,k)

def swap(i,j):
    global a
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def partition(s,e):
    global a
    
    if s+1 == e:
        if a[s] > a[e]:
            swap(s,e)
    
    m = (s+e)//2
    swap(s,m)
    pivot = a[s]
    i = s+1
    j = e
    print(a)
    while i<= j:
        while pivot < a[j] and j>0: j-= 1; print("j=",j,end=" ")
        while pivot > a[i] and i<len(a)-1: i+=1; print("i=",i," ")

        if i<=j:
            swap(i,j)
            i+=1
            j-=1
            
    a[s] = a[j]
    a[j] = pivot
    print(a,j,i)
    return j

quickSort(0, n-1, m-1)
print(a[m-1])
```


-------------------------------------------------------------------------------------------

034. { 수를 묶어서 최댓값 만들기 } 179p

> 우선순위 큐를 이용하여 4그룹으로 만듦<br>
(양수) , (1) , (0) , (음수)<br>
각 우선순위큐에 양수와 음수를 넣고<br>
서로 곱함. 수가 하나씩 남아있으면 더하고, 음수는 0이있다면 곱함

```
from queue import PriorityQueue

n = int(input().split())
plus = PriorityQueue()
minus = PriorityQueue()
one = 0
zero = 0

for i in range(n):
    data = int(input())
    
    if data > 1:
        plus.put(data *- 1)	#오름차순을 위해 음수로 바꿔줌
    elif data == 1: one += 1
    elif data == 0: zero += 1
    else : minus.put(data)
    
sum = 0

while plus.qsize() > 1:
    first = plus.get() *- 1
    second = plus.get()* -1
    sum += first * second
    
if plus.qsize > 0:
    sum += plus.get()*-1
    
while minus.qsize > 1:
    first = minus.get()
    second = minus.get()
    sum += first * second

if minus.qsize > 0:	#0이 남아있지않으면 나머지 음수를 더함
    if zero == 0:
        sum += minus.get()
    
sum += one

print(sum)
```

-------------------------------------------------------------------------------------------
++{ 소수 구하기 } 193p

```
import math
m,n = map(int, input().split())

a = [0]*(n+1)
for i in range(2,n+1):
    a[i] = i;

for i in range(2, int(math.sqrt(n)+1)):
    if a[i] == 0:
        continue;
    for j in range(i+i,n+1,i):
        a[j]=0

for i in range(m,n+1):
    if a[i] != 0: print(a[i])
```

-------------------------------------------------------------------------------------------
038. { 거의 소수 구하기 } 196p
> 2^7까지 소수 배열을 미리 생성한 뒤,  소수에 n제곱을 이용하여 범위 포함이면 res++

```
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
        while a[i] <= max/tmp:	#제곱근으로 곱하면 정수표현을 넘어가기에 나누기로 표현
            if a[i] >= min/tmp:
                res+=1
            tmp *= a[i]
print(res)
```

-------------------------------------------------------------------------------------------

041. { 오일러 피함수 구하기 } 207p
이거 진짜 모르겟음
```
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
 ```
-------------------------------------------------------------------------------------------

042. {최소 공배수 구하기} 211p
유클리드 호제법으로 최대 공약수를 구하고

```
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b,a%b) #최소공약수
        

n = int(input())

for i in range(n):
    a,b = map(int, input().split())
    res = a * b / gcd(a,b)	#a 와 b 를 곱하고 최소공약수로 나누면 = 최대 공배수
    print(int(res))
```

-------------------------------------------------------------------------------------------

043.{ 최대 공약수 구하기 } 226p

```
def gcd(a,b):
    if b == 0: return a
    else : return gcd(b,a%b)
    
a, b = map(int, input().split())
res = gcd(a,b)

for i in range(res):
    print(1,end="")
```
    
