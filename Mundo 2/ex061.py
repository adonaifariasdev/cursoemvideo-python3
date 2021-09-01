# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('-='*10)
print('{:^20}'.format('GERADOR DE PA'))
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
n = (primeiro + (10 - 1) * razao) + 1
while primeiro < n:
    print(primeiro, end=' -> ')
    primeiro = primeiro + razao
print('FIM')

# Forma do Guanabara abaixo:
'''primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont += 1
print('FIM')'''

