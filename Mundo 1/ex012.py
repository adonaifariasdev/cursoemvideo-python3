preco = float(input('Digite o preço do produto: R$'))
novoPreco = preco - (preco * (5/100))
print('O preço do produto com 5% de desconto é R${:.2f}.'.format(novoPreco))

