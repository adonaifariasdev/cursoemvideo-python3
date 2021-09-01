# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# Forma abaixo de calcular o Fatorail bem simples com uma funcao
'''from math import factorial
n =int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))'''

from time import sleep
fat = 1
num = int(input('Digite um número para\ncalcular seu Fatorial: '))
sleep(0.3)
print('Calculando {}! = '.format(num), end='')
while num > 1:
    print('{} x '.format(num), end='')
    sleep(0.3)
    fat = fat * num
    num = num - 1
print('1 = {}'.format(fat))
