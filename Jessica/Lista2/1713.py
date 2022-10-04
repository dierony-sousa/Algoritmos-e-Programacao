# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valorHora = float(input())
horasTrabalhadas = float(input())

salarioBruto = valorHora * horasTrabalhadas
imposto = salarioBruto * 11 / 100
inss = salarioBruto * 8 / 100
sindicato = salarioBruto * 5 / 100
salarioLiquido = salarioBruto - imposto - inss - sindicato

print("Salário bruto: R$%.2f" %(salarioBruto))
print("Imposto:  R$%.2f" %(imposto))
print("INSS: R$%.2f" %(inss))
print("Sindicato: R$%.2f" %(sindicato))
print("Líquido: R$%.2f" %(salarioLiquido))
