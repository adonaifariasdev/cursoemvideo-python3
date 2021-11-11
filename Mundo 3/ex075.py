# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

n1 = n2 = n3 = n4 = 0
for c in range(1, 5):
    num = int(input('Digite um valor: '))
    if c == 1:
        n1 = num
    elif c == 2:
        n2 = num
    elif c == 3:
        n3 = num
    elif c == 4:
        n4 = num
    valores = (n1, n2, n3, n4)
print(f'Você digitou os valores {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes')
print(f'O valor 3 apareceu na {valores.index(3)+1}a. posição') # Dando erro pois tem que
#fazer acondição if 3 in valores como no ex075a
print(f'Os valores pares digitados foram ', end='')
for c in valores:
    if c % 2 == 0:
        print(c, end=' ... ')

