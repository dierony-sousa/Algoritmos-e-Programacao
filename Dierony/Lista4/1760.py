# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

p = 0
somaIdade = 0
pesoG = 0
for p in range(4):
    idade = int(input())
    peso = float(input())
    somaIdade += idade
    if peso > 90:
        pesoG += 1

media = somaIdade / 4

print('Qtd pessoas > 90 Kg: {}'.format(pesoG))
print('Idade média: {:.2f}'.format(media))
