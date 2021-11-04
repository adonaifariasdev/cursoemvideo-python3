# Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

'''extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenve', 'vinte')'''
# FORMA DO GUANABARA
cont =  ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenve', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end='')
print(f'Você digitou o número {cont[num]}')

# FORMA DO ADONAI!
'''num = -1
while num not in range(0, 21):
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <=20:
        print(f'Você digitou {extenso[num]}')
    else:
        print('Digite novamente.', end='')'''