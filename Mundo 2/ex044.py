# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('='*40)
loja = ' SUPER LOJÃO DA MIMI '
print('{:=^40}'.format(loja)) #### pode ser feito assim tb print('{:=^40}'.format(' SUPERLOJÃO DA MIMI ')
print('='*40)
preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque (10% de Desconto)
[ 2 ] à vista cartão (5% de Desconto)
[ 3 ] 2x no cartão (SEM JUROS)
[ 4 ] 3x ou mais no cartão (20% de JUROS)''')
opcao = int(input('Qual opção: '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    valorParcela = preco / 2
    total = preco
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(valorParcela))
elif opcao == 4:
    numParcelas = int(input('Quantas parcelas? '))
    total = preco + (preco * 20 / 100)
    valorParcela = total / numParcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(numParcelas, valorParcela))
else:
    total = preco
    print('OPÇÃOINVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
