from random import *
num_secreto = randint(0,10)
tentativas = 0
chute = 0

while chute != num_secreto:
    tentativas += 1
    chute = int(input("Digite um número de 0 a 100: "))
    if chute == num_secreto:
        print("Parabéns, você acertou em %d tentativas" %tentativas)
    elif chute > num_secreto:
        print("O número sorteado é menor")
    else:
        print("O número sorteado é maior")

        
