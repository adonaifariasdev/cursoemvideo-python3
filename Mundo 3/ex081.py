# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    r = ''
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break

print(f'Você digitou {len(numeros)} números.')
numeros.sort(reverse=True)
print(f'A lista de números decrescente é: {numeros}')
if 5 in numeros:
    print('O número 5 foi digitado!')
else:
    print('O número 5 não foi digitado!')
