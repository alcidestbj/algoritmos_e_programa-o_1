nomes = [] #ou nomes = list()
for i in range(5):
    n = input("Digite um nome: ")
    nomes.append(n)  

print(nomes)
print(len(nomes))

#exclui um item da lista
nome = input("Digite um nome para remover da lista: ")
if nome in nomes:
  nomes.remove(nome) 
  print(nomes) 
  print(len(nomes))
else:
  print("Nome não encontrado!")

  
