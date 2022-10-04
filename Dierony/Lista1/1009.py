# https://www.beecrowd.com.br/judge/pt/problems/view/1009

NOME = str(input())
SALARIO = float(input())
VENDAS = float(input())

TOTAL = SALARIO + (VENDAS * 15 / 100)

print("TOTAL = R$ {:.2f}".format(TOTAL))
