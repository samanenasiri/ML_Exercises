def max_int(num):
    num,max_num=str(num),0
    for i in range(len(num)-1) :
        m=int(num.replace(num[i]+num[i+1],str(int(num[i])+int(num[i+1]))))
        if m > max_num:
            max_num = m
    return max_num        
print(max_int(10038))