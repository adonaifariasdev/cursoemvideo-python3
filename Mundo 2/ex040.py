# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
print('Tirando {} e {}, a média é {:.1f}.'.format(n1, n2, media))
if media < 5 and media >= 0:
    print('O aluno está REPROVADO.')
elif media >= 5 and media < 7: # if 7 > media >= 5 <- Pode ser assim tb.
    print('O aluno está de RECUPERAÇÃO.')
elif media >= 7 and media <= 10:
    print('O aluno está APROVADO.')
else:
    print('Valores inválidos! Digite novamente as notas!')
