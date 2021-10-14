from ex116.lib.interface import *
from ex116.lib.arquivo import *
from time import sleep

cabeçalho('CRIAR UM AQUIVO TXT')
nome = str(input('Digite o nome do arquivo para abrir ou para cria-lo: '))
arq = nome + '.txt'

if not arquivoExiste(arq):
    criaArquivo(arq)
else:
    print(f'O arquivo ({arq}) já existe!')
    print(f'Abrindo arquivo {arq} ...')
    sleep(2)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do programa'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('CADASTRAR NOVA PESSOA')
        nome = str(input('Nome: ')).upper()
        idade = leiInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('SAINDO DO PROGRAMA')
        print('Aqui sairá do programa!')
        break
    else:
        print('\033[31mERRO! Digige uma opção válida!\033[m')
    sleep(2)
