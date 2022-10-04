# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

valComp = float(input())

if valComp < 20.00:
  lucro = valComp * (45/100)
  valVend = lucro + valComp
  print("Valor de venda: R$%.2f" %(valVend))

else:
  lucro = valComp * (30/100)
  valVend = lucro + valComp
  print("Valor de venda: R$%.2f" %(valVend))
