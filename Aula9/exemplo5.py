
import funcoes_ex5

a = int(input("Digite A: "))
b = int(input("Digite B: "))

op = int(input("1-Soma\n2-Subtração\nDigite uma opção: "))
if op == 1:
    print(funcoes_ex5.somaValores(a,b))
elif op == 2:
    print(funcoes_ex5.subtraiValores(a,b))
else:
    print("Opção inválida")

funcoes_ex5.fim()

