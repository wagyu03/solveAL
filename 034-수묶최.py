from queue import PriorityQueue

n = int(input().split())
plus = PriorityQueue()
minus = PriorityQueue()
one = 0
zero = 0

for i in range(n):
    data = int(input())
    
    if data > 1:
        plus.put(data *- 1)
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

if minus.qsize > 0:
    if zero == 0:
        sum += minus.get()
    
sum += one

print(sum)