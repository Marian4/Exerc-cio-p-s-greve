def valorPagamento(ValorPresta�ao,DiasAtraso):
  presta��es = 0
  total = 0
  while ValorPresta�ao > 0:
    if DiasAtraso == 0:
      ValorASerPago = ValorPresta�ao
      print("Valor a ser pago: %.2f"%ValorASerPago)
      presta��es += 1
      total += ValorASerPago
      ValorPresta�ao = eval(input("Qual o valor da presta��o a ser paga?"))
      DiasAtraso = eval(input("Quantos dias o pagamento est� atrasado?"))
    elif DiasAtraso > 0:
      multa = (ValorPresta�ao/100)*3
      juros =((ValorPresta�ao/100)*0.1)*DiasAtraso
      ValorASerPago = ValorPresta�ao + multa + juros
      print("Valor a ser pago:%.2f"%ValorASerPago)
      presta��es += 1 
      total += ValorASerPago
      ValorPresta�ao = eval(input("Qual o valor da presta��o a ser paga?"))
      DiasAtraso = eval(input("Quantos dias o pagamento est� atrasado?"))
  print("\nPrograma encerrado.\n")
  print("Relat�rio do dia:\n\nPresta��es pagas:%i\nTotal pago:%.2f"%(presta��es,total))
print("O programa ser� encerrado quando o valor da presta��o for 0.\n")
ValorPresta�ao = eval(input("Qual o valor da presta��o a ser paga?"))
DiasAtraso = eval(input("Quantos dias o pagamento est� atrasado?"))
valorPagamento(ValorPresta�ao,DiasAtraso)
