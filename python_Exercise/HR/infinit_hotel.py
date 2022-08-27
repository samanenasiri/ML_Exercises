
k = int(input("group size: "))
rooms = list(map(int, input("rooms number: ").split()))
rooms_dict= {}
for i in rooms:
    if  i not in rooms_dict:
        rooms_dict[i] = 1
    else:
        rooms_dict[i] += 1
print(rooms_dict)        
for key, val in rooms_dict.items():
    if val != k:
        print(key)


