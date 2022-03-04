print('-'*40)
print('{:^40}'.format('Lista De Preços'))
print('-'*40)
produtos = ("Lápis", 1.75, "Borracha", 2.00, "Caderno",
            15.90, "Estojo", 25.00, "Transferidor", 4.20,
            "Compasso", 9.99, "Mochila", 120.32, "Canetas",
            22.30, "Livro", 34.90)

for pos, p in enumerate(produtos):
    if pos % 2 == 0:
        print('{:.<20}'.format(p), end='')
    else:
        print('R${:>7.2f}'.format(p))
print('-'*40)
