# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Que ano quer analisar(yyyy)?\nColoque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #coloca o ano tual da maquina importado da biblioteca datetime
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ANO {} É BISSEXTO!'.format(ano))
else:
    print('O ANO {} NÃO BISSEXTO!'.format(ano))
