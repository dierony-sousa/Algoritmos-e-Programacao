# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

tipoCliente = int(input())
valorCompra = float(input())
vCompraFunc = valorCompra - (valorCompra * 13 / 100)
vCompraPrem = valorCompra - (valorCompra * 7 / 100)

if (tipoCliente == 1):
  print("Valor total a ser pago: R$%.2f" %(valorCompra))
elif (tipoCliente == 2):
  print("Valor total a ser pago: R$%.2f" %(vCompraFunc))
elif (tipoCliente == 3):
  print("Valor total a ser pago: R$%.2f" %(vCompraPrem))
else:
  print("OPÇÃO INVÁLIDA!")
