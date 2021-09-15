def BinarySearchRecursive (A, left, right, x):
    if left > right:
          return -1
    mid= (left+right)//2
    if A[mid]==x:
          return mid
    if A[mid]>x:
          return BinarySearchRecursive (A, left, mid-1, x)
    if A[mid]<x:
          return BinarySearchRecursive (A, mid+1, right, x)

A=[2,3,7,9,10,22,23,26,28,30]
n=len(A)
x=28
result=BinarySearchRecursive(A,0,n-1,x)
if result==-1:
    print("Not found %d"%x)
else:
    print("found %d at index %d" % (x,result))