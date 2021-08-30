nomeFull = str(input('Digitre seu nome completo: ')).strip()
nomeDividido = nomeFull.split()
print('Primeiro nome: {}.'.format(nomeDividido[0]))
print('Último nome: {}.'.format(nomeDividido[len(nomeDividido) - 1]))
