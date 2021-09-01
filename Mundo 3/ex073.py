# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino',
         'Corinthians', 'Atlético-GO', 'Ceará', 'Athletico-PR', 'Internacional',
         'Santos', 'São Paulo', 'Juventude', 'Cuiabá', 'Bahia',
         'Fluminense', 'Grêmio', 'Sport Recife', 'América-MG', 'Chapecoense')
print('=' * 35)
print(f'Lista  de times do Brasileirão 2021: {times}')
print('=' * 35)
print(f'Os 5 primeiros são: {times[0:5]}')
print('=' * 35)
print(f'Os 4 últimos são: {times[-4:]}')
print('=' * 35)
print(f'Times em ordem alfabético: {sorted(times)}')
print('=' * 35)
print(f'O Santos está na', times.index('Santos')+1, end='a. posição.\n')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}a. posição')
print('=' * 35)
for pos, time in enumerate(times):
    print(f'{(pos)+1}a. -> {time}')

