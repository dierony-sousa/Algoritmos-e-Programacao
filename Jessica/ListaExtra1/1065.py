#https://www.beecrowd.com.br/judge/pt/problems/view/1065

par = 0

for i in range(5):
    n = int(input())
    if n % 2 == 0:
        par += 1

print('%i valores pares'%(par))
