# Faça um programa que tenha uma função chamada área(), que receba as dimensões de 
# um terreno retangular
# (largura e comprimento) e mostre a área do terreno.

def area(x, y):
    a = x * y
    print(f'A Área de um terreno de {x:.1f}x{y:.1f} é de {a:.1f}m2.')


#Programa Principal
print('Controle de  Terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
