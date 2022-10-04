# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

precoCompra = float(input())

if (precoCompra < 20):
  valorVenda = precoCompra + (precoCompra*45/100)
else:
  valorVenda = precoCompra + (precoCompra*30/100)

print("Valor de venda: R$%.2f" %(valorVenda))

