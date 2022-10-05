# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

cont = (int(input()))
num = 0
soma = 0

if cont > 0:
  while cont > 0:
    num = float(input())
    soma = soma + num
    cont = cont -1
  print('Soma dos números informados: %.2f'%(soma))
else:
  print('Informe uma quantidade > 0!')
