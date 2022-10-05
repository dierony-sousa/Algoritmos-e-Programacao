# https://www.beecrowd.com.br/judge/pt/problems/view/1045

def decrescente(x, y, z):
    if x >= y >= z:
        A = x
        B = y
        C = z
        return [A, B, C]

    elif x >= z >= y:
        A = x
        B = z
        C = y
        return [A, B, C]

    elif y >= x >= z:
        A = y
        B = x
        C = z
        return [A, B, C]

    elif y >= z >= x:
        A = y
        B = z
        C = y
        return [A, B, C]

    elif z >= x >= y:
        A = z
        B = x
        C = y
        return [A, B, C]

    elif z >= y >= x:
        A = z
        B = y
        C = x
        return [A, B, C]


A = float(input())
B = float(input())
C = float(input())

[a, b, c] = decrescente(A, B, C)

if a >= b + c:
    print('NAO FORMA TRIANGULO')

elif a**2 == b**2 + c**2:
    print('TRIANGULO RETANGULO')

elif a**2 > b**2 + c**2:
    print('TRIANGULO OBTUSANGULO')

elif a**2 < b**2 + c**2:
    print('TRIANGULO ACUTANGULO')

if a == b == c:
    print('TRIANGULO EQUILATERO')

elif a == b or b == c or a == c:
    print('TRIANGULO ISOSCELES')
