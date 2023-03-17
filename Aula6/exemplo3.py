
contador = 0
soma = 0
resp = "s"

while resp == "s":
    num = float(input("Digite um número: "))
    soma = soma + num
    contador = contador + 1
    resp = input("Deseja continuar (S ou N)? ").lower()

media = soma / contador
print("A média dos números digitados é %.2f" %media)

