quatpizza = eval(input("digite a quantidade de pizzas: "))

prepizza = eval(input("digite o pre�o das pizzas: "))

valorpizz = quatpizza * prepizza

imposto = (valorpizz / 100) * 8

valortotal = valorpizz + imposto

print ("valor a ser pago :", valortotal)
