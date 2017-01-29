def coverterMin(Minutos):
  minutos = Minutos
  horas = 0
  while minutos >= 60:
    horas += 1
    minutos -= 60
  dias = 0 
  while horas >= 24:
    dias += 1
    horas -= 24
  anos = 0 
  while dias >= 365:
    anos += 1
    dias -= 365
  print("Você perdeu",end=" ")
  if anos > 0:
    print("%i anos"%anos,end=" ")
  if dias > 0 and anos == 0:
    print("%i dias"%dias,end=" ")
  elif dias > 0 and anos > 0:
    if horas > 0 and minutos > 0:
      print(",%i dias"%dias,end=" ")
    elif horas == 0 and minutos == 0:
      print("e %i dias"%dias,end=" ")
  if horas > 0 and (dias > 0 or anos > 0):
    if minutos > 0:
      print(",%i horas"%horas,end=" ")
    elif minutos == 0:
      print("e %i horas"%horas,end=" ")
  elif horas > 0 and dias == 0 and anos == 0:
    print("%i horas"%horas,end=" ")
  if minutos > 0:
    print("e %i minutos"%minutos,end=" ")
  if minutos == 0 and horas == 0 and dias == 0 and anos == 0:
    print("0",end="")
  print("de vida.")
cigDia = eval(input("Quantos cigarros você fuma por dia em média?"))
anosfum = eval(input("A quantos anos você fuma?"))
dias = anosfum*365
cigarros = cigDia*dias
Minutos = cigarros*10
coverterMin(Minutos)