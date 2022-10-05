# https://www.beecrowd.com.br/judge/pt/problems/view/1065

p = 0
for c in range(5):
    n = int(input())
    if n % 2 == 0:
        p += 1

print('{} valores pares'.format(p))
