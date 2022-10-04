# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

tipoPlano = input()
salarioAtual = float(input())
planoA = salarioAtual + (salarioAtual * 10 /100)
planoB =  salarioAtual + (salarioAtual * 15 /100)
planoC =  salarioAtual + (salarioAtual * 20 /100)

if (tipoPlano == 'A'):
  print("Novo salário: R$%.2f" %(planoA))
elif (tipoPlano == 'B'):
  print("Novo salário: R$%.2f" %(planoB))
elif (tipoPlano == 'C'):
  print("Novo salário: R$%.2f" %(planoC))
