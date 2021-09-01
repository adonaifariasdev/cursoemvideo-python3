# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.


from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
soma = totVit = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    soma = jogador + computador
    # opcao = ' ' -> na situaçao se for colocar o comando While, conforme resolução do Guanabara
    opcao = str(input('Par ou ÍMPAR? [P/I] ')).upper().strip()[0] # Se colocar um while not in 'PI': -> se qualquer outro caractere digitado voltará a perguntar
    print('-'*30)
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU PAR')
    else:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} DEU ÍMPAR')
    print('-' * 30)
    if opcao == 'P' and soma % 2 == 0:
        totVit += 1
        print('Você VENCEU!!!')
        print('Vamos jogar novamente...')
        print('-=' * 15)
    elif opcao == 'I' and soma % 2 != 0:
        totVit += 1
        print('Você VENCEU!!!')
        print('Vamos jogar novamente...')
        print('-=' * 15)
    else:
        print('Você PERDEU!!!')
        print('-=' * 15)
        break
print(f'GAME OVER! Você venceu {totVit} vezes.')
