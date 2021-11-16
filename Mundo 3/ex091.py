# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário
# em ordem,
# sabendo que o vencedor tirou o maior número no dado.
from random import randint
resultados = dict()
rank = []
resultados['jogador1'] = randint(1, 6)
resultados['jogador2'] = randint(1, 6)
resultados['jogador3'] = randint(1, 6)
resultados['jogador4'] = randint(1, 6)
print('-=' * 40)
print(f'Os resultados são: {resultados}')
print('-=' * 40)
for k, v in resultados.items():
    print(f'{k:30} tirou {v:30} no dado.')
    rank.append(v)
print('-=' * 40)
print(f'{"== RANKING DOS JOGADORES ==":^80}')
print('-=' * 40)
ranking = sorted(rank, reverse=True)
print(ranking)
