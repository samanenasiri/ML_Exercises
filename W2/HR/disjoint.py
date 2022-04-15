
n, m = map(int, input("n(size of array) and m(size of A and B) :").strip().split(' '))
array=[]
for i in range(n):
    arr= input("array:")
    array.append(arr)
A=[]
for i in range(m):
    a= input("A:")
    A.append(a)
B=[]    
for i in range(m):
    b= input("B:")
    B.append(b)
happiness = 0
for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)