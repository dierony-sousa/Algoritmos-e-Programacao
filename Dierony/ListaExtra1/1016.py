# https://www.beecrowd.com.br/judge/pt/problems/view/1016

velX = 60
velY = 90
tempo = 60

dist = int(input())

tempo = dist / ((velY/60)-(velX/60))

print('{:.0f} minutos'.format(tempo))
