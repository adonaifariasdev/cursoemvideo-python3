# Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# Pedindo pro usuário se ele quer continuar.

cont =  ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenve', 'vinte')
while True:
    num = int(input('Digite um nùmero entre 0 e 20: '))
    
    if num >= 0 and num <= 20:
        print(f'Você digitou {cont[num]}')
        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp == 'N':
            break
    else:
        print('Tente novamente.', end='')


