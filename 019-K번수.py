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


