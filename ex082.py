lista = []
par = []
impar = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if num % 2 != 0:
        impar.append(num)
    else:
        par.append(num)
    if op == 'N':
        break
print('-='*30)
print(f'A lista completa é: {lista}')
print(f'A lista de números pares é: {par}')
print(f'A lista de números impares é: {impar}')
