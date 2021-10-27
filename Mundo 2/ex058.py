# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
computador = randint(0, 10)
totJogadas = 0
print('-=-'*20)
print('{:^60}'.format(' JOGO DE ADIVINHAÇÃO 2.0 '))
print('-=-'*20)
print('Vou pensa em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? '))
#print('PROCESSANDO....')
#sleep(2)
while jogador != computador:

    if jogador > computador:
        print('Menos...', end='')
    else:
        print('Mais...', end='')
    jogador = int(input('Em que número eu pensei? '))
    totJogadas += 1
print('Eu escolhi o número {}. Você GANHOU na {}a. tentativa!\nParabéns!!!'
      .format(computador, totJogadas + 1))
print('-=-'*20)
print('{:^60}'.format(' DEVELOPED BY ADONAI VALMONT '))
print('{:^60}'.format(' oficialadonai@hotmail.com '))
print('{:^60}'.format(' ALL RIGHTS RESERVED 2021'))
print('-=-'*20)
