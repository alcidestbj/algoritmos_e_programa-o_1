import math

a = float(input("Informe o coeficiente A: "))
b = float(input("Informe o coeficiente B: "))
c = float(input("Informe o coeficiente C: "))

delta = b**2 - 4*a*c

if delta < 0 :
    print("Não há raízes reais para esta equação.")
else:
    if delta == 0:
        x = (-b) / (2*a)
        print("As duas raízes da equação são iguais, seu valor é", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("A raiz 1 é", x1, " e a raiz 2 é", x2)

#testes
#a=1, b=-5, c=6 ==> r1=3 e r2=2
#a=4, b=-4, c=1 ==> r1=r2= ???
#a=5, b=1, c=6 ==> não há como encontrar raízes para essa equação em R 
