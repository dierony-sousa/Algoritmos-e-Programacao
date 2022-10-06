#https://www.beecrowd.com.br/judge/pt/problems/view/1074

n = int(input())

for i in range(n):
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
