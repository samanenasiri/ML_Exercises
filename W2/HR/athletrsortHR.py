n = int(input("Enter number of athlete : "))
l=[]
for i in range(0,n):

       a = list(map(int,input("\nEnter the informations  : ").strip().split()))
       l.append(a)

k=int(input('k:'))
def takeindex(l):
    return l[k]
l.sort(key=takeindex)    
for i in l :
    print(*i)




  