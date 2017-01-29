base = int(input("digite o número da base: "))

expoente = int(input("digite o número do expoente: "))

calculo = base**expoente

print ("base:", base)

print ("expoente:", expoente)

print(base,"elevado a",expoente,"=",base,"",end="")

for j in range(expoente - 1):

  print("x",base,"",end="")

print("=",calculo)
