from ast import Num
from re import A


B = []

for i in range(0,3):
    num = int(input('Enter a number : '))
    if(num > 10 and num < 20):
        B.append(num)
    else:
        print('Invalid Number !')    
print(B)

def insertionSort(B):
    for i in range(1,len(B)):
        key = B[i]
        j = i -1
        while j >=0 and key <B[j]:
            B[j+1] = B[j]
            j = j-1
        B[j+1] = key

insertionSort(B)
print('Sorted Array : ', B)
