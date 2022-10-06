#https://www.beecrowd.com.br/judge/pt/problems/view/1021

n = float(input())

if 0 <= n <= 1000000:

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

    n = float('{:.2f}'.format(n))
    if int(n/100) >= 1:
        n100 = int(n/100)
        n -= n100 * 100

    n = float('{:.2f}'.format(n))
    if int(n/50) >= 1:
        n50 = int(n/50)
        n -= n50 * 50

    n = float('{:.2f}'.format(n))
    if int(n/20) >= 1:
        n20 = int(n/20)
        n -= n20 * 20

    n = float('{:.2f}'.format(n))
    if int(n/10) >= 1:
        n10 = int(n/10)
        n -= n10 * 10

    n = float('{:.2f}'.format(n))
    if int(n/5) >= 1:
        n5 = int(n/5)
        n -= n5 * 5

    n = float('{:.2f}'.format(n))
    if int(n/2) >= 1:
        n2 = int(n/2)
        n -= n2 * 2

    n = float('{:.2f}'.format(n))
    if int(n/1) >= 1:
        m1 = int(n/1)
        n -= m1 * 1

    n = float('{:.2f}'.format(n))
    if int(n/0.50) >= 1:
        m050 = int(n/0.50)
        n -= m050 * 0.50

    n = float('{:.2f}'.format(n))
    if int(n/0.25) >= 1:
        m025 = int(n/0.25)
        n -= m025 * 0.25

    n = float('{:.2f}'.format(n))
    if int(n/0.1) >= 1:
        m010 = int(n/0.1)
        n -= m010 * 0.1

    n = float('{:.2f}'.format(n))
    if int(n/0.05) >= 1:
        m005 = int(n/0.05)
        n -= m005 * 0.05

    n = float('{:.2f}'.format(n))
    if int(n/0.01) >= 0.01:
        m001 = int(n/0.01)
        n -= m001 * 0.01

    print('NOTAS:')
    print('%i nota(s) de R$ 100.00'%(n100))
    print('%i nota(s) de R$ 50.00'%(n50))
    print('%i nota(s) de R$ 20.00'%(n20))
    print('%i nota(s) de R$ 10.00'%(n10))
    print('%i nota(s) de R$ 5.00'%(n5))
    print('%i nota(s) de R$ 2.00'%(n2))
    print('MOEDAS:')
    print('%i moeda(s) de R$ 1.00'%(m1))
    print('%i moeda(s) de R$ 0.50'%(m050))
    print('%i moeda(s) de R$ 0.25'%(m025))
    print('%i moeda(s) de R$ 0.10'%(m010))
    print('%i moeda(s) de R$ 0.05'%(m005))
    print('%i moeda(s) de R$ 0.01'%(m001)))
