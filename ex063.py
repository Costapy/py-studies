print('-'*15)
print('Sequência de Fibonacci')
print('-'*15)
ter = int(input('Quantos termos deseja mostrar? '))
pos = 3
n1 = 0
n2 = 1
prox = 0
print('{} ➔ {} ➔ '.format(n1,n2), end='')

while pos <= ter:
    prox = n1 + n2
    print('{} ➔ '.format(prox), end='')
    pos += 1
    while 3 < pos <= ter:
        n1 = n2
        n2 = prox
        prox = n1 + n2
        print('{} ➔ '.format(prox), end='')
        pos += 1
print('FIM')
