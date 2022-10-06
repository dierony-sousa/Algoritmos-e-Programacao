#https://www.beecrowd.com.br/judge/pt/problems/view/1061

diaInicial = int(input().split()[-1])
horaInicial, minInicial, segInicial = map(int, input().split(' : '))

diaFinal = int(input().split()[-1])
horaFinal, minFinal, segFinal = map(int, input().split(' : '))

dias = diaFinal - diaInicial
horas = horaFinal - horaInicial
min = minFinal - minInicial
seg = segFinal - segInicial

if seg < 0:
    seg += 60
    min -= 1

if min < 0:
    min += 60
    horas -= 1

if horas < 0:
    horas += 24
    dias -= 1

print('%i dia(s)'%(dias))
print('%i hora(s)'%(horas))
print('%i minuto(s)'%(min))
print('%i segundo(s)'%(seg))

