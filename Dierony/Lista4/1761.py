# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

    i = 1
    total = 0

    while True:
        preco = float(input())
        i += 1
        total += preco
        if preco == 0:
            break
    
    valPago = float(input())

    print("Total da compra: R${:.2f}".format(total))
    print("Valor pago: R${:.2f}".format(valPago))
    print("Troco: R${:.2f}".format(valPago - total))

    break
