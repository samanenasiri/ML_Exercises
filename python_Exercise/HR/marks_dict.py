n = int(input("Enter number of student : "))
my_dict={}
for i in range(0,n):
    name,*score=input("name and scores:").split()

    my_dict[name]=score
print(my_dict)
query_list=list(map(float,my_dict[input('query_name:')]))
mean=sum(query_list)/len(query_list)
print("%.2f" % mean )






