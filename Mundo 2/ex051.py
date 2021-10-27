# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

print('='*40)
print('{:^40}'.format('10 TERMOS DE UMA PA'))
print('='*40)
'''p1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for c in range(0, 10):
    print(p1, end=' -> ')
    p1 = p1 + r
print('ACABOU')'''

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')
