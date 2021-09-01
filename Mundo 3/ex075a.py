# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um nùmero: ')),
       int(input('Digite outro nùmero: ')),
       int(input('Digite mais um nùmero: ')),
       int(input('Digite o último nùmero: ')))
print(f'Você digitou os valores {num}')
print(f'O nùmero 9 foi digitado {num.count(9)} vez(es)')
if 3 in num:
       print(f'O primeiro valor 3 digitado foi na {num.index(3)+1}a. posição')
else:
       print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')


