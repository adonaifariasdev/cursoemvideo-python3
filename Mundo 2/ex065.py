# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

opcao = 'S'
maior = menor = cont = media = soma = 0
while opcao != 'N': # Pelo Guanabara foi utilizado while resp in 'Ss':
    num = int(input('Digite um número: '))
    opcao = str(input('Deseja continuar? [S/N]')).upper().strip()
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print('Você digitou {} valores e a média foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
