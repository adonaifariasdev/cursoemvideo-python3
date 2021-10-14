# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep
def cabeçalho():
    cab = 'SISTEMA DE AJUDA PyHELP'
    tam = len(cab) + 4
    print('\033[0;42m~' * tam)
    print(f'\033[0;42m{cab:^{tam}}')
    print(f'\033[0;42m~' * tam)


def cabeçalhoAzul():
    cab = f"Acessando o manual do comando '{funcao}'"
    tam = len(cab) + 4
    print('\033[0;44m~' * tam)
    print(f'\033[0;44m{cab:^{tam}}')
    print(f'\033[0;44m~' * tam)


def pyHelp(func):
    print(f'\033[7;40m')
    return help(func)


# Programa Principal
while True:
    cabeçalho()
    funcao = str(input('\033[mFunção ou Biblioteca > '))
    if funcao == 'fim':
        break
    else:
        cabeçalhoAzul()
        sleep(1)
        pyHelp(funcao)

