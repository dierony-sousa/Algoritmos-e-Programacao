# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

plano = input()
salAt = float(input())

if plano == "A":
  salNv = salAt + salAt * (10/100)
  print("Novo salário: R$%.2f" %(salNv))

elif plano == "B":
  salNv = salAt + salAt * (15/100)
  print("Novo salário: R$%.2f" %(salNv))

elif plano == "C":
  salNv = salAt + salAt * (20/100)
  print("Novo salário: R$%.2f" %(salNv))
