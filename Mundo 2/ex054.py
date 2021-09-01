# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
maiorIdade = 0
menorIdade = 0
for c in range(1, 8):
    anoNasc = int(input('{}) Qual seu ano de nascimento:'.format(c)))
    idade = date.today().year - anoNasc
    if idade >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1
print('{} pessoas já atingiram a maioridade!'.format(maiorIdade))
print('{} pessoas não atingiram a maioridade!'.format(menorIdade))
