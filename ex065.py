maior = menor = cont = soma = 0
prog = 'S'

while prog == 'S':
    num = int(input('Digite um Número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    prog = str(input('Deseja Continuar? [S/N]: ')).upper().strip()[0]
média = soma/cont
print('O maior foi {} e o menor {} já a média foi igual a {:.2f}'.format(maior, menor, média))
