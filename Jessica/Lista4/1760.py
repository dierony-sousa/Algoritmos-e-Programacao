# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

qtdPessoas = 0
mediaIdades = 0

for n in range(4):
  idade = int(input())
  peso = float(input())
  mediaIdades = mediaIdades + idade

  if (peso > 90):
    qtdPessoas +=1

mediaIdades = mediaIdades / 4

print("Qtd pessoas > 90 Kg: %i"%(qtdPessoas))
print("Idade média: %.2f"%(mediaIdades))
