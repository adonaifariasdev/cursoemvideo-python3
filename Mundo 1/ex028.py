from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente Adivinhar...')
print('--='*20)
usuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO.......')
sleep(2)
print('Eu escolhi o número {}.'.format(computador))
if usuario == computador:
    print('PARABÉNS! VOCÊ CONSEGUIU ME VENCER!')
else:
    print('SINTO MUITO! VOCÊ NÃO ME VENCEU!!')
