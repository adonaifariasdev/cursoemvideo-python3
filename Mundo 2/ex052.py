#  Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um número pra saber se é primo: '))
cont = 0
for c in range(num, 0, -1):
    if num % 2 != 0 and num % c == 0 and num % 1 == 0:
        cont = cont + 1
    if num == 1 or num == 2:
        cont = 2
if cont == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')