# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
maior = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('>>>>> Qual é a sua opção? '))
    if opcao == 1:
        print('A soma entre {} + {} é {}.'.format(n1, n2, n1 + n2))
        print('-=-'*10)
    elif opcao == 2:
        print('A multiplicação entre {} x {} é {}.'.format(n1, n2, n1 * n2))
        print('-=-'*10)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        else:
            print('Os números são iguais!')
        print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
        print('-=-' * 10)
    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao != 5:
        print('Opção inválida. Tente novamente.')
        print('-=-' * 10)
print('Finalizando...')
print('-=-' * 10)
sleep(2)
print('Fim do programa! Volte sempre!')
