x,y,z,n, = int(input('x:')),int(input('y:')),int(input('z:')),int(input('n:'))

#_______________________________________
resault = []
for X in range(x+1):
    for Y in range(y+1):
        for Z in range(z+1):
            if X+Y+Z != n:
                xyz = [X,Y,Z];
                resault.append(xyz);
print(resault)   

#_________________________________________________________________
print([[X,Y,Z]  for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X+Y+Z!=n])