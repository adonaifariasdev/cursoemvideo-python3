# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('=' * 30)
print(f'{ "JOGA NA MEGA SENA ":^30}')
print('=' * 30)
n = int(input('Quantos jogos quer sortear? '))
print('-' * 30)
print(f'{"SORTEANDO JOGOS...":^30}')
print('-' * 30)
sleep(2)
for c in range(0, n):
    jogos = [randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)]
    print(f'Jogo {c+1}: {sorted(jogos)}')
    sleep(0.4)
print(f'{" < BOA SORTE > ":=^30}')