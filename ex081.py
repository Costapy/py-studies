lista = []

while True:
    num = lista.append(int(input('Digite um valor: ')))
    op = str(input('Desja continuar? [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Desja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print('-='*30)
print(f'A lista teve um total de {len(lista)} elementos digitados.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}')
if 5 in lista:
    print('O valor 5 está presente na lista!')
else:
    print('O valor 5 não foi encontrado na lista')
