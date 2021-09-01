# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print('{:=^20}'.format(' JO KEN PÔ '))
print('Suas opções: ')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogador = int(input('Qual a sua jogada? '))
computador = randint(0, 2)
sleep(0.5)
print('JO..')
sleep(0.5)
print('KEN..')
sleep(0.5)
print('PÔ')
sleep(0.5)
print('-='*20)
print('{:^40}'.format('JO KEN PÔ'))
print('-='*20)

if jogador == 0 and computador == 0:
    jogador = 'PEDRA'
    computador = 'PEDRA'
    print('        Computador jogou {}'.format(computador))
    print('        Jogador jogou {}'.format(jogador))
    print('-=' * 20)
    print('{:^40}'.format('EMPATE!'))

elif jogador == 1 and computador == 1:
    jogador = 'PAPEL'
    computador = 'PAPEL'
    print('        Computador jogou {}'.format(computador))
    print('        Jogador jogou {}'.format(jogador))
    print('-=' * 20)
    print('{:^40}'.format('EMPATE!'))

elif jogador == 2 and computador == 2:
    jogador = 'TESOURA'
    computador = 'TESOURA'
    print('        Computador jogou {}'.format(computador))
    print('        Jogador jogou {}'.format(jogador))
    print('-=' * 20)
    print('{:^40}'.format('EMPATE!'))

elif jogador == 0 and computador == 1:
    jogador = 'PEDRA'
    computador = 'PAPEL'
    print('        Computador jogou {}'.format(computador))
    print('        Jogador jogou {}'.format(jogador))
    print('-=' * 20)
    print('{:^40}'.format('Computador VENCE!'))

elif jogador == 0 and computador == 2:
    jogador = 'PEDRA'
    computador = 'TESOURA'
    print('        Computador jogou {}'.format(computador))
    print('        Jogador jogou {}'.format(jogador))
    print('-=' * 20)
    print('{:^40}'.format('Jogador VENCE!'))

elif jogador == 1 and computador == 0:
    jogador = 'PAPEL'
    computador = 'PEDRA'
    print('        Computador jogou {}'.format(computador))
    print('        Jogador jogou {}'.format(jogador))
    print('-=' * 20)
    print('{:^40}'.format('Jogador VENCE!'))

elif jogador == 1 and computador == 2:
    jogador = 'PAPEL'
    computador = 'TESOURA'
    print('        Computador jogou {}'.format(computador))
    print('        Jogador jogou {}'.format(jogador))
    print('-=' * 20)
    print('{:^40}'.format('Computador VENCE!'))

elif jogador == 2 and computador == 0:
    jogador = 'TESOURA'
    computador = 'PEDRA'
    print('        Computador jogou {}'.format(computador))
    print('        Jogador jogou {}'.format(jogador))
    print('-=' * 20)
    print('{:^40}'.format('Computador VENCE!'))

elif jogador == 2 and computador == 1:
    jogador = 'TESOURA'
    computador = 'PAPEL'
    print('        Computador jogou {}'.format(computador))
    print('        Jogador jogou {}'.format(jogador))
    print('-=' * 20)
    print('{:^40}'.format('Jogador VENCE!'))
else:
    print('    Jogada INVÁLIDA! Tente novamente.')
print('-=' * 20)
