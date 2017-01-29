lista = []
adicionar =eval(input("Adicionar um nome a lista?(1)-sim,(2)não:"))
while adicionar == 1:
  adicionando = str(input("Escreva um nome e um sobrenome:"))
  lista.append(adicionando)
  adicionar =eval(input("Adicionar um nome a lista?(1)-sim,(2)não:"))
numero = len(lista)
string = ""
for i in range(numero):
  string += lista[i] + " "
novaLista = string.split()
print()
for j in range(len(novaLista)):
  if j%2 == 1:
    print(novaLista[j],end=",")
    print(novaLista[j-1],end=";")
