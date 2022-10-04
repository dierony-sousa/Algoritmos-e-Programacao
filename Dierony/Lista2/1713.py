# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valHora = float(input())
horaTab = float(input())

salBrut = valHora * horaTab

impRenda = salBrut * (11/100)
inss = salBrut * (8/100)
sind = salBrut * (5/100)

desc = impRenda + inss + sind
salLiq = salBrut - desc

print("Salário Bruto: R$%.2f" %(salBrut))
print("Imposto: R$%.2f" %(impRenda))
print("INSS: R$%.2f" %(inss))
print("Sindicato: R$%.2f" %(sind))
print("Líquido: R$%.2f" %(salLiq))
