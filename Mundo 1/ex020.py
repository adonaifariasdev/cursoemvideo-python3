#import random
from random import shuffle
n1 = str(input('Digite o nome do Aluno 1: '))
n2 = str(input('Digite o nome do Aluno 2: '))
n3 = str(input('Digite o nome do Aluno 3: '))
n4 = str(input('Digite o nome do Aluno 4: '))
lista = [n1, n2, n3, n4]
#random.shuffle(lista)
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))
