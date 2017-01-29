numero = int(input("digite o número: "))

fatorial = 1

if (numero > 0):
 
 for i in range (1, numero+1):
 
   fatorial = fatorial * i

print ("fatorial de", numero,":", fatorial)
