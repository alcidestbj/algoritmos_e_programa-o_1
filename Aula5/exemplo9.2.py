a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if (a < b):
    if (b < c):
        print(a,b,c)
    elif (a < c):
        print(a,c,b)
    else:
        print(c,a,b)
else:
    if (a < c):
        print(b,a,c)
    elif (b < c):
        print(b,c,a)
    else:
        print(c,b,a)




    
