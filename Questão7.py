def valorPagamento(ValorPrestaçao,DiasAtraso):
  prestações = 0
  total = 0
  while ValorPrestaçao > 0:
    if DiasAtraso == 0:
      ValorASerPago = ValorPrestaçao
      print("Valor a ser pago: %.2f"%ValorASerPago)
      prestações += 1
      total += ValorASerPago
      ValorPrestaçao = eval(input("Qual o valor da prestação a ser paga?"))
      DiasAtraso = eval(input("Quantos dias o pagamento está atrasado?"))
    elif DiasAtraso > 0:
      multa = (ValorPrestaçao/100)*3
      juros =((ValorPrestaçao/100)*0.1)*DiasAtraso
      ValorASerPago = ValorPrestaçao + multa + juros
      print("Valor a ser pago:%.2f"%ValorASerPago)
      prestações += 1 
      total += ValorASerPago
      ValorPrestaçao = eval(input("Qual o valor da prestação a ser paga?"))
      DiasAtraso = eval(input("Quantos dias o pagamento está atrasado?"))
  print("\nPrograma encerrado.\n")
  print("Relatório do dia:\n\nPrestações pagas:%i\nTotal pago:%.2f"%(prestações,total))
print("O programa será encerrado quando o valor da prestação for 0.\n")
ValorPrestaçao = eval(input("Qual o valor da prestação a ser paga?"))
DiasAtraso = eval(input("Quantos dias o pagamento está atrasado?"))
valorPagamento(ValorPrestaçao,DiasAtraso)
