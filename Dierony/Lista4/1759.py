# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

ano = 2005
sal = 1000

anoAtual = int(input())
aumento = 1.5 / 100

if anoAtual > 2005:
    while ano < anoAtual:
        sal *= 1 + aumento
        aumento += 1/100
        ano += 1

    print('Salário atual: R${:.2f}'.format(sal))

else:
    print('O ano informado deverá ser > 2005!')
