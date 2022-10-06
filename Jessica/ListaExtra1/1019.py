#https://www.beecrowd.com.br/judge/pt/problems/view/1019

n = int(input())


h = n // 60**2
n = n - h * 60**2
m = n // 60
n = n - m*60

print("%i:%i:%i" %(h, m,n))
