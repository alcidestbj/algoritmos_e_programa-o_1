def calculaArea(b, a):
    return b * a/2

base = float(input("Digite a base do triângulo em cm: "))
altura = float(input("Digite a altura do triângulo em cm: "))

print("A área do triângulo é %.2f cm²" % calculaArea(base,altura))
print("Podemos chamar a função diversas veses")
print(calculaArea(8,5))
print(calculaArea(10,10))
print(calculaArea(2,5))
