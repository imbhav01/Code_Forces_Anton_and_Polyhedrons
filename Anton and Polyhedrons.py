x = int(input())
count = 0
for i in range(0,x):
    y = str(input())
    if (y=="Tetrahedron"):
        count = count+4
    elif (y=="Cube"):
        count = count+6
    elif (y=="Octahedron"):
        count = count+8    
    elif (y=="Dodecahedron"):
        count = count+12
    elif (y=="Icosahedron"):
        count = count+20

print(count)