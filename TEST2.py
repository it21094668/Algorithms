
A=[]
for v in range(1,4):
    num = int(input('Enter number : '))
    A.append(num)

print('Unsorted Array : ',A)

def selectionSort(A):
    n = len(A)
    for j in range(0,n-1):
        smallest = j
        for i in range(j+1,n):
            if A[i]<A[smallest]:
                smallest = i
            A[j],A[smallest] = A[smallest],A[j]

selectionSort(A)

print('Sorted Array : ',A)
