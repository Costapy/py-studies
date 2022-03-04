valores = []
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado... Não irei adicionar')
    else:
        print('Valor adicionado com sucesso...')
        valores.append(num)
    op = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    while op not in 'SsNn':
        op = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if op == 'N':
        break
print('-='*30)
valores.sort()
print(f'Você digitou os números {valores}')
