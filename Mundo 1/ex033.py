# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
# Aumentei para 4 números.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
d = int(input('Digite o terceiro número: '))
# Verificando quem é menor
menor = a
if b < a and b < c and b < d:
    menor = b
if c < a and c < b and c < d:
    menor = c
if d < a and d < b and d < c:
    menor = d
# Verificando quem é maior
maior = a
if b > a and b > c and b > d:
    maior = b
if c > a and c > b and c > d:
    maior = c
if d > a and d > b and d > c:
    maior = d
print('O menor número digitado é {}.'.format(menor))
print('O maior número digitado é {}.'.format(maior))
