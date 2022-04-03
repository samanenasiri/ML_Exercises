
num='?0'
def is_well_defined(num):
    
    flag=[]
    num, my_dict=list(num),{"1":"0","0":"1"}
    for indexes in range(len(num)):
        while num[indexes]=='?':
            for key,value in my_dict.items():
                    if num[indexes-1]==key:
                        num[indexes]=value  
                    else:
                        num[indexes]='0'
    complete_num="".join(num) 
    print(complete_num)                                                 
    for indexes in range(len(complete_num)-1):
        if complete_num[indexes]==complete_num[indexes+1]:
                        flag.append(1)
    if len(flag)>0:
        return False 
    else:
        return True
print(is_well_defined(num))             








num='1?1'
flag=[]
def is_well_define(num):
    if '?' not in num:
        for i in range(len(num)-1):
            if '00' not in num and '11' not in num:
                flag.append(1)
    else:
        for i in range(len(num)):
            if num[i]=='?':
                temp1=num[:i]+"1"+num[i+1:] 
              
                is_well_define(temp1)
                temp2=num[:i]+"0"+num[i+1:] 
               
                is_well_define(temp2) 


    if len(flag)>0:
        return True
    else:
        return False
print(is_well_define(num))








 


