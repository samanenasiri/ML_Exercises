import operator
import functools
mat1 = [[1,1,2,2],[3,3,4,4],[5,5,6,6],[7,7,8,8]]
mat2 = [[5,5,5,5],[6,6,6,6],[7,7,7,7],[8,8,8,8]]


def split(matrix):
    a = matrix
    b = matrix
    c = matrix
    d = matrix
    while(len(a) > len(matrix)/2):
        a = a[:len(a)//2]
        b = b[:len(b)//2]
        c = c[len(c)//2:]
        d = d[len(d)//2:]
    while(len(a[0]) > len(matrix[0])/2):
        for i in range(len(a[0])//2):
            a[i] = a[i][:len(a[i])//2]
            b[i] = b[i][len(b[i])//2:]
            c[i] = c[i][:len(c[i])//2]
            d[i] = d[i][len(d[i])//2:]
    return a,b,c,d
print(split(mat1))    



def add(mat1, mat2):
   
    d = []
    for i in range(len(mat1)):
        c = []
        for j in range(len(mat1[0])):
            c.append(mat1[i][j] + mat2[i][j])
        d.append(c)
    return d



def multiply(mat1,mat2):
    satr_mat1=len(mat1)
    sotoon_mat1=len(mat1[0])
 

    satr_mat2=len(mat2)
    sotoon_mat2=len(mat2[0])                  


    if  satr_mat1==sotoon_mat2 :
        my_mat = []
        for i in range(satr_mat1):
            list1=[]
            for j in range(sotoon_mat2):
                list2=[]
                for k in range(sotoon_mat1):
                    list2.append(mat1[i][k]*mat2[k][j])      
                list1.append(functools.reduce(operator.add,list2))
            my_mat.append(list1)    
        return my_mat



def sub(mat1, mat2):
   
    d = []
    for i in range(len(mat1)):
        c = []
        for j in range(len(mat1[0])):
            c.append(mat1[i][j] - mat2[i][j])
        d.append(c)
    return d



def strassen(mat1, mat2):
 
    a, b, c, d = split(mat1)
    e, f, g, h = split(mat2)

    p1 = multiply(a,(sub(f,h)))

    p2 = multiply(add(a,b),h)

    p3 = multiply(add(c,d),e)

    p4 = multiply(d,sub(g,e))

    p5 =multiply( add(a,d),add(e,h))

    p6 =multiply( sub(b,d),add(g,h))

    p7 =multiply( sub(a,c) , add(e,f))

    c11 = add(sub(add(p5, p4), p2), p6)

    c12 = add(p1, p2)

    c21 = add(p3, p4)

    c22 = sub(sub(add(p1, p5), p3), p7)
    c = [[0 for i in range(len(mat1))] for j in range(len(mat1))]

    for i in range(len(c11)):
        for j in range(len(c11)):
            c[i][j]                   = c11[i][j]
            c[i][j+len(c11)]          = c12[i][j]
            c[i+len(c11)][j]          = c21[i][j]
            c[i+len(c11)][j+len(c11)] = c22[i][j]

    return c      


print(strassen(mat1,mat2))