# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
            'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')


for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c]} temos: ', end='')
    for index, letra in enumerate(palavras[c]):
        if letra.lower() in 'aeiou':
            print(f'{letra.lower()} ', end='')
        '''if letra == 'A':
            print(f'{letra} ', end='')
        if letra == 'E':
            print(f'{letra} ', end='')
        if letra == 'I':
            print(f'{letra} ', end='')
        if letra == 'O':
            print(f'{letra} ', end='')
        if letra == 'U':
            print(f'{letra} ', end='')'''
