
import trigonometria as tri

catO = float(input("Digite o cateto oposto: "))
catA = float(input("Digite o cateto adjascente: "))

print("O seno é: %.2f" % tri.seno(catO, catA))
print("O cosseno é: %.2f" % tri.cosseno(catO, catA))
print("A tangente é: %.2f" % tri.tangente(catO, catA))

