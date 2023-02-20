import math

num = float(input("Digite um número: "))
absoluto = math.fabs(num)
inteiro = math.trunc(num)
raiz = math.sqrt(absoluto)
fatorial = math.factorial(math.fabs(inteiro))

print("Valor absoluto:", absoluto)
print("Parte inteira V1:", inteiro)
print("Raiz:", raiz)
print("Fatorial:",fatorial)

