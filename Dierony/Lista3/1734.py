# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

N = int(input())
c = N
x = 1

while c > 0:
  x = x * c
  c = c - 1
print('%i! = %i' %(N, x))
