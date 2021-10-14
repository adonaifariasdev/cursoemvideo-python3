# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date
def voto(anoNasc):
    idade = date.today().year - anoNasc
    if idade < 16:
        voto = 'NÃO VOTA'
    elif idade >= 16 and idade < 18 or idade >= 70:
        voto = "VOTO OPCIONAL"
    elif idade >= 18 and idade < 70:
       voto = 'VOTO OBRIGATÓRIO.'
    print(f'Com {idade} anos: {voto}')


# Programa Principal
anoNasc = int(input('Em que ano você nasceu? '))
voto(anoNasc)
