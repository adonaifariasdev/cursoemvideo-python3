n = int(input('Digite um número para saber seu Fatorial: '))
f = 1
print('Calculando {}! = '.format(n), end='')
for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)