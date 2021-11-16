# Crie um programa que leia nome e duas notas de vários alunos e guarde 
# tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que 
# o usuário possa mostrar as
# notas de cada aluno individualmente.

lista = []
relacao = []
cont = 1
print('-=' * 30)
print(f'{"ESCOLA DE ENSINO PROFISSIONALIZANTE VALMONT":^60}')
print('-=' * 30)
print(f'{"CADASTRO DE ALUNOS E NOTAS DO BOLETIM ":^60}')
while True:
    print('-' * 60)
    print('<' * 5, f'                 CADASTRO No. {cont}                 ', '>' * 5)
    print('-' * 60)
    nome = str(input('Nome do Aluno: '))
    lista.append(nome)
    nota1 = float(input('Nota 1: '))
    lista.append((nota1))
    nota2 = float(input('Nota 2: '))
    lista.append(nota2)
    media = (nota1 + nota2) / 2
    lista.append(media)
    relacao.append(lista[:])
    lista.clear()
    cont += 1

    resp = str(input('Quer continuar? [S/N]'))[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print('No. NOME                 MÉDIA')
print('-' * 30)
for c in range(0, len(relacao)):
    print(f'{c:<2}', f'{relacao[c][0]:<22}', f'{relacao[c][3]:<4}')
print('-' * 30)

while True:
    item = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe) '))

    if item == 999:
        break
    print(f'Notas de {relacao[item][0]} são: {relacao[item][1], relacao[item][2]}')
    print('-' * 30)
print('FINALIZANDO...')
print('>>>VOLTE SEMPRE<<<')


