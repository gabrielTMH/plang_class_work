def countdown(n):
    if n==0:
        return
    print(n)
    countdown(n-1)

def countdown(n):
    while True:
        if n==0:
            return
        print(n)
        n-=1

def fact(n):
    if n==1:
        return 1
    return n* fact(n-1)

def fact(n,product=1):
    if n==1:
        return product
    return fact(n-1,n*product)

def fect(n):
    product=1
    while True:
        if n==1:
            return product
        product*=n
        n-=1

class Cons:
   def __init__(self, head, tail=None):
       self.head = head
       self.tail = tail

def contains(ls, x):
   if ls is None:
       return False
   if x == ls.head:
       return True
   return contains(ls.tail, x)

def contains(ls,x):
    while ls.tail != None:
        if x ==ls.head:
            return True
        ls=ls.tail
    return False


def length(ls):
   if ls is None:
       return 0
   return 1 + length(ls.tail)

def length(ls,acc=0):
    if ls is None:
        return acc
    return length(ls.tail,acc+1)




def length(ls):
    if ls is None:
        return 0
    else:
        prod=1
        while ls.tail != None:
            prod+=1
            ls=ls.tail
        return prod


def partition(a, lo, hi):
   p = a[lo]
   small = [x for x in a[lo+1:hi] if x < p]
   large = [x for x in a[lo+1:hi] if x >= p]
   a[lo:hi] = small + [p] + large
   return lo + len(small)

def quicksort(a, lo=0, hi=None):
   if hi is None:
       hi = len(a)
   if hi - lo <= 1:
       return
   mid = partition(a, lo, hi)
   quicksort(a, lo, mid)
   quicksort(a, mid + 1, hi)

def quicksort(a, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    if hi- lo <= 1:
        return
    mid = partition(a,lo,hi)
    newMid = mid
    while newMid>lo:
        newMid = partition(a,lo,newMid)
    quicksort(a,mid+1,hi)

a=[10,98,11,5,1000,6,32,108,9,3]
quicksort(a)
print(a)
