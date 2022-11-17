
A= []

for v in range(1,4):
    num = int(input('Enter your number : '))
    A.append(num)
print(A)

def insertionSort(A):
    n = len(A)
    for j in range(0,n):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] =key

insertionSort(A)
print('Sorted Array :',A)