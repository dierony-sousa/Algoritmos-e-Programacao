# https://www.beecrowd.com.br/judge/pt/problems/view/1021

valor = float(input())

if 0 <= valor <= 1000000.00:

    n100 = 0
    n50 = 0
    n20 = 0
    n10 = 0
    n5 = 0
    n2 = 0
    m1 = 0
    m050 = 0
    m025 = 0
    m010 = 0
    m005 = 0
    m001 = 0

    valor = float('{:.2f}'.format(valor))
    if int(valor/100) >= 1:
        n100 = int(valor/100)
        valor -= n100 * 100

    valor = float('{:.2f}'.format(valor))
    if int(valor/50) >= 1:
        n50 = int(valor/50)
        valor -= n50 * 50

    valor = float('{:.2f}'.format(valor))
    if int(valor/20) >= 1:
        n20 = int(valor/20)
        valor -= n20 * 20

    valor = float('{:.2f}'.format(valor))
    if int(valor/10) >= 1:
        n10 = int(valor/10)
        valor -= n10 * 10

    valor = float('{:.2f}'.format(valor))
    if int(valor/5) >= 1:
        n5 = int(valor/5)
        valor -= n5 * 5

    valor = float('{:.2f}'.format(valor))
    if int(valor/2) >= 1:
        n2 = int(valor/2)
        valor -= n2 * 2

    valor = float('{:.2f}'.format(valor))
    if int(valor/1) >= 1:
        m1 = int(valor/1)
        valor -= m1 * 1

    valor = float('{:.2f}'.format(valor))
    if int(valor/0.50) >= 1:
        m050 = int(valor/0.50)
        valor -= m050 * 0.50

    valor = float('{:.2f}'.format(valor))
    if int(valor/0.25) >= 1:
        m025 = int(valor/0.25)
        valor -= m025 * 0.25

    valor = float('{:.2f}'.format(valor))
    if int(valor/0.1) >= 1:
        m010 = int(valor/0.1)
        valor -= m010 * 0.1

    valor = float('{:.2f}'.format(valor))
    if int(valor/0.05) >= 1:
        m005 = int(valor/0.05)
        valor -= m005 * 0.05

    valor = float('{:.2f}'.format(valor))
    if int(valor/0.01) >= 0.01:
        m001 = int(valor/0.01)
        valor -= m001 * 0.01

    print('NOTAS:')
    print('{} nota(s) de R$ 100.00'.format(n100))
    print('{} nota(s) de R$ 50.00'.format(n50))
    print('{} nota(s) de R$ 20.00'.format(n20))
    print('{} nota(s) de R$ 10.00'.format(n10))
    print('{} nota(s) de R$ 5.00'.format(n5))
    print('{} nota(s) de R$ 2.00'.format(n2))
    print('MOEDAS:')
    print('{} moeda(s) de R$ 1.00'.format(m1))
    print('{} moeda(s) de R$ 0.50'.format(m050))
    print('{} moeda(s) de R$ 0.25'.format(m025))
    print('{} moeda(s) de R$ 0.10'.format(m010))
    print('{} moeda(s) de R$ 0.05'.format(m005))
    print('{} moeda(s) de R$ 0.01'.format(m001))
