
num='10?101??'
def is_well_defined(num):
    num, my_dict=list(num),{"1":"0","0":"1"}
    for indexes in range(len(num)):
        while num[indexes]=='?':
            for key,value in my_dict.items():
                    if num[indexes-1]==key:
                        num[indexes]=value  
    complete_num="".join(num)                                                  
    for indexes in range(len(complete_num)-1):
        if complete_num[indexes]==complete_num[indexes+1]:
            return False  
print(is_well_defined(num))


