# https://www.beecrowd.com.br/judge/pt/problems/view/1019

N = int(input())
horas = N // 60**2
N = N - horas * 60**2

minutos = N // 60
N = N - minutos*60

segundos = N

print('{}:{}:{}'.format(horas, minutos, segundos))
