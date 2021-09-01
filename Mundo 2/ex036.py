# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep
print('-='*20)
print('|  BANCO DE FINANCIAMENTO IMOBILIÁRIO  |')
print('-='*20)
valorCasa = float(input('Qual o valor do imóvel? R$ '))
salComprador = float(input('Qual o valor do seu salário? R$ '))
qtdeAnos = int(input('Em quantos anos irá pagar? '))
qtdeMeses = qtdeAnos * 12
prestMensal = valorCasa / qtdeMeses
trintaSal = salComprador * (30 / 100)
print('PROCESSANDO...')
sleep(3)
print('-='*20)
print('|        STATUS DO FINANCIAMENTO       |')
print('-='*20)
print(' VALOR DO IMÓVEL R${:.2F}'.format(valorCasa))
print(' QTDE ANOS: {}  | QTDE MESES: {}'.format(qtdeAnos, qtdeMeses))
print(' SALÁRIO R${:.2f} | 30% SALÁRIO R${:.2f}'.format(salComprador, trintaSal))
print(' VALOR DA PRESTAÇÃO R${:.2f}'.format(prestMensal))
if prestMensal > trintaSal:
    print(' EMPRÉSTIMO NEGADO.')
else:
    print(' EMPRÉSTIMO APROVADO.')
