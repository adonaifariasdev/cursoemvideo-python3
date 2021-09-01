# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
from time import sleep
valor = int(input('Que valor você que sacar? R$'))
total = valor
céd = 50
totcéd = 0
print('AGUARDE...CONTANDO CÉDULAS...')
sleep(2)
while True:
    if total >= céd: #Verifica se o total ainda é maior que o valor 50
        total -= céd #Vai diminuindo o valor total
        totcéd += 1 #Vai contando o número de cédulas possiveis de tirar do total do valor
    else:
        if totcéd > 0:
            sleep(1)
            print(f'Total {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
