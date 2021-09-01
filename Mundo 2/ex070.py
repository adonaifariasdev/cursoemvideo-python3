# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total = maisMil = 0
cont = caro = barato = 0
produtoBarato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        maisMil += 1

    cont += 1
    if cont == 1:
        caro = preco
        barato = preco
        produtoBarato = produto
    else:
        if preco > caro:
            caro = preco
        if preco < barato:
            barato = preco
            produtoBarato = produto

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if opcao == 'N':
        break
print(f'Total: {total:10.2f}.')
print(f'Temos {maisMil} produto(s) que custa(m) mais de R$1000.00.')
print(f'O produto mais barato foi "{produtoBarato}" e custou R${barato:.2f}.')
