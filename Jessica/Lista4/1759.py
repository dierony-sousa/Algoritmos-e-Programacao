# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

salario = 1000
aumento = 1.5
anoInicial = 2006
anoAtual = int(input())

if (anoAtual < 2006):
    print("O ano informado deverá ser > 2005!")
else:
    while anoInicial <= anoAtual:
        salario = salario + (salario * aumento / 100)
        aumento = aumento + 1
        anoInicial += 1
    print("Salário atual: R$%.2f" % (salario))
