def BinarySearch (A, n, x):
    low = 0
    high = n - 1
    while low<=high:
        mid=(low+high)//2
        if A[mid]==x:
            return mid
        elif A[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1

A=[2,3,7,9,10,22,23,26,28,30]
n=len(A)
x=100
result=BinarySearch(A,n,x)
if result==-1:
    print("Not found %d"%x)
else:
    print("found %d at index %d" % (x,result))