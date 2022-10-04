# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

total = 0
valor = float(input())

while (valor != 0):
  total = total + valor
  valor = float(input())

valorPago = float(input())
troco = valorPago - total

print("Total da compra: R$%.2f"%(total))
print("Valor pago: R$%.2f"%(valorPago))
print("Troco: R$%.2f"%(troco))
