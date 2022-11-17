A = []

for v in range (1,5):
    num = int(input("Enter your number : "))
    A.append(num)

print(A)

def bubbleSortDesc(A):
    n = len(A)

    for i in range(1,n):
        for j in range(1,n-i+1):
            if A[j] > A[j-1]:
                A[j],A[j-1] = A[j-1],A[j]

bubbleSortDesc(A)

print("Sorted Array : ",A)