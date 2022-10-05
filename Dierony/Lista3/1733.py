# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = str(input())
horExtr = float(input())

salMin = 1192.40
valHorExtr = 10.00

salHorExtr = horExtr * valHorExtr
salBrut = 3 * salMin + salHorExtr

if salBrut > 2000:
  descINSS = salBrut * (12/100)
else:
  descINSS = salBrut * (5/100)

if salBrut > 2500:
  descIR = salBrut * (20/100)
else:
  descIR = 0

salLiq = salBrut - descINSS - descIR

print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(salBrut))
print("Salário líquido: R$%.2f" %(salLiq))
