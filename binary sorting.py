import math
def binarySearch(arr,i,r,x):

    while i<=r:

        mid = i + (r-i)/2
        mid=math.floor(mid)

        if arr[mid] ==x:
            return mid

        elif arr[mid]<x:
            i = mid+1

        else:
            r=mid-1

    return -1


arr = [2,3,4,10,40]
x = int(input("Enter a number"))

result = binarySearch(arr,0,len(arr)-1,x)

if result != -1:
    print("Element is present in indexn %d" %result)
else:
    print("Element is not present in index")
