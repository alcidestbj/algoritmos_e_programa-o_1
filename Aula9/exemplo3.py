def calculaIMC(p, a):    
    return (p / a**2 )

def despedida():
    print("Obrigado por usar este programa!")
    print("Até logo!")

peso = float(input("Digite o peso da pessoa, em Kg: "))
altura = float(input("Digite a estatura da pessoa, em m: "))
print("O IMC é ", calculaIMC(peso,altura), " Kg/m²")
despedida()


