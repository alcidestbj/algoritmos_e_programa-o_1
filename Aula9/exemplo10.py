
soma = lambda a,b: a + b
subt = lambda a,b: a - b
mult = lambda a,b: a * b
divi = lambda a,b: a / b


print("Calculadora lambda")
print("[1] Soma\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n[0] Sair")
while True:
    op = int(input("Digite uma opção: "))
    if op == 0:
        break
    elif str(op) not in '1234':
        print("Opção inválida")
    else:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        if op == 1:
            print(soma(x,y))
        elif op == 2:
            print(subt(x,y))
        elif op == 3:
            print(mult(x,y))
        else:
            print(divi(x,y))
            
        
        
