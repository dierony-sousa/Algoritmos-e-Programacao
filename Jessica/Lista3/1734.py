# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

n = int(input())
contador = n
fatorial = 1

while contador > 1:
  fatorial = fatorial * contador
  contador = contador - 1

print("%i! = %i"%(n,fatorial))
