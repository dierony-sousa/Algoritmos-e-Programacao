# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nomeFuncionario = input()
horasExtras = float(input())

salHoraExtra = horasExtras * 10
salBruto = (3 *1192.40) + salHoraExtra;

if salBruto > 2000:
  descINSS = salBruto * 12 / 100
else :
  descINSS = salBruto * 5 / 100

if salBruto > 2500:
  descImpRenda = salBruto * 20 / 100
else:
 descImpRenda = 0

salLiquido = salBruto - descINSS - descImpRenda

print("Nome: %s" %(nomeFuncionario))
print("Salário bruto: R$%.2f" %(salBruto))
print("Salário líquido: R$%.2f" %(salLiquido))
