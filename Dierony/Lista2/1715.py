# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

codID = int(input())
valTotal = float(input())

if codID == 1:
  valPag = valTotal
  print("Valor total a ser pago: R$%.2f" %(valPag))

elif codID == 2:
  desc = valTotal * (13/100)
  valPag = valTotal - desc
  print("Valor total a ser pago: R$%.2f" %(valPag))

elif codID == 3:
  desc = valTotal * (7/100)
  valPag = valTotal - desc
  print("Valor total a ser pago: R$%.2f" %(valPag))

else:
  print("OPÇÃO INVÁLIDA!")
