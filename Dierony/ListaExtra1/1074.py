# https://www.beecrowd.com.br/judge/pt/problems/view/1074

N = int(input())

for c in range(N):
    num = int(input())
    if num == 0:
        print('NULL')

    elif num % 2 == 0:
        print('EVEN', end=' ')

    elif num % 2 != 0:
        print('ODD', end=' ')

    if num > 0:
        print('POSITIVE')

    elif num < 0:
        print('NEGATIVE')
