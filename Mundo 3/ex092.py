# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['anoNasc'] = int(input('Ano de Nascimento: '))
idade = date.today().year - dados['anoNasc']
dados['idade'] = idade
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
while True:
    if dados['ctps'] == 0:
        print('-=' * 30)
        del dados['anoNasc']
        for k, v in dados.items():
            print(f' - {k} tem o valor {v}.')
        break
    else:
        dados['contratação'] = int(input('Ano de Contratação: '))
        dados['salario'] = float(input('Salário: '))
        dados['aposentadoria'] = (dados['contratação'] - dados['anoNasc']) + 35
        del dados['anoNasc']
        print('-=' * 30)
        for k, v in dados.items():
            print(f' - {k} tem o valor {v}.')
        break
