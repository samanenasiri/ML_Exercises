def remove_local_max():
    mylist,count =[int(x) for x in input("enter your list:").split()] , 0
    for i in range(len(mylist)-1):
        if mylist[i-1]<mylist[i]>mylist[i+1]:
            mylist[i+1]=max(mylist[i],mylist[i+2])
            count+=1
    print(mylist)    
    return count 
print(remove_local_max()) 