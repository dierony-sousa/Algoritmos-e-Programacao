# https://www.beecrowd.com.br/judge/pt/problems/view/1017

consumo = 12

tempo = int(input())
vel = int(input())

litros = tempo * vel / consumo

print('{:.3f}'.format(litros))
