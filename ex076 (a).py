print('-'*40)
print('{:^40}'.format('Lista De Preços'))
print('-'*40)

produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno",
            15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas",
            22.30, "Livro", 34.90)
cont = 0
while True:
    print('{:.<20} '.format(produtos[cont]), end='')
    cont += 1
    print('R${:>7.2f}'.format(produtos[cont]))
    cont += 1
    if cont >= 17:
        break
print('-'*40)
