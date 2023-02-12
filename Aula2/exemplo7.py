# Exemplo 7 - Cálculo do IMC
peso = float(input("Digite o peso da pessoa (em kg): "))
altura = float(input("Digite a altura da pessoa (em m): "))
imc = peso / altura**2
print("O IMC da pessoa é: %f kg/m²"%(imc))
