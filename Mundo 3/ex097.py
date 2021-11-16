# Faça um programa que tenha uma função chamada escreva(), que receba um texto
# qualquer como parâmetro e
# mostre uma mensagem com tamanho adaptável.
# Ex:
# escreva(‘Olá, Mundo!’) Saída:
# ~~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~~

def escreva(texto):
    tam = len(texto) + 4
    print('~' * tam)
    print(f'{texto:^{tam}}')
    print('~' * tam)


#Programa Principal
mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)
escreva('Adonai Valmont')

