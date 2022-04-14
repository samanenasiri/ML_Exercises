
def print_formatted(number):
    result2=[]
    for i in range(1, number+1):
        result1=[]
        result1.append(str(i))
        result1.append(oct(i)[2:])
        result1.append(hex(i)[2:])
        result1.append(bin(i)[2:])
        result2.append(result1)   
    print(result2)
    for l in result2:
        print(*l)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)        


   