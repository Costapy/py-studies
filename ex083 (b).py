exp = str(input('Digite uma expressão: '))
lista = list()

for val in exp:
    if val == '(':
        lista.append('(')
    elif val == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) > 0:
    print('A expressão possui algum erro.')
else:
    print('A expressão está correta!')
