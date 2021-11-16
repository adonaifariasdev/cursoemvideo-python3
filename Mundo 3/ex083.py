# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
# abertos e fechados na ordem correta.
c = cont = 0
expr = str(input('Digite uma expressão: '))
for v in expr:
    if v == '(':
        c += 1
    elif v == ')':
        cont += 1
if c == cont:
    print('Sua expressão está válida!')
elif c != cont:
    print('Sua espressão está errada!')

# Versao muito limitada!
