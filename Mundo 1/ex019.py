import random
n1 = input('Digite o nome do Aluno 1: ')
n2 = input('Digite o nome do Aluno 2: ')
n3 = input('Digite o nome do Aluno 3: ')
n4 = input('Digite o nome do Aluno 4: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O Aluno escolhido para apagar o quadro foi {}.'.format(escolhido))
