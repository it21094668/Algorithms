A=[]

for v in range(4):
    A.append(int(input('Enter number : ')))
print('Unsorted Array : ', A)

x = int(input('Enter your search value : '))

def binarySearch(A, low,high,x):
    if high >= low:
        mid = (high + low) // 2

        if A[mid] == x:
            return mid
        
        elif A[mid] > x:
            return binarySearch(A,low,mid-1,x)
        
        else:
            return binarySearch(A,mid+1,high,x)

    else:
        return -1

#function call

result = binarySearch(A,0,len(A)-1,x)
if result != -1:
    print('Element is present in index', str(result))

else:
    print('Element is not present in array')