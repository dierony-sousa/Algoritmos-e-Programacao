# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

qtdNumeros = int(input())
soma = 0

if qtdNumeros <= 0:
  print("Informe uma quantidade > 0!")
else:
  while qtdNumeros > 0:
    soma = soma + float(input())
    qtdNumeros = qtdNumeros - 1

  print("Soma dos números informados: %.2f"%(soma))
