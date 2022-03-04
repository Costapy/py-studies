lista = []
exp = str(input('Escreva a expressão: '))

for val in exp:
    lista.append(val)
if lista.count('(') != lista.count(')'):
    print('A expressão apresenta algum erro.')
else:
    print('A expressão está correta!')
