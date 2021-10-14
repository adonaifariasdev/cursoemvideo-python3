exp = str(input('Digite uma expressao: '))
expressao = []
for simb in exp:
    if simb == '(':
        expressao.append('(')
    elif simb == ')':
        if len(expressao) > 0:
            expressao.pop()
        else:
            expressao.append(')')
            break
if len(expressao) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua espressão está errada!')

