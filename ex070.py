print('-'*15)
print('LOJA COSTA')
print('-'*15)
soma = cont = contma = pmenor = 0
nmenor = ' '

while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    soma += preço
    if preço > 1000:
        contma += 1
    if cont == 1:
        pmenor = preço
        nmenor = nome
    if preço < pmenor:
        pmenor = preço
        nmenor = nome
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(f'''O valor total da compra foi de R${soma:.2f}
Existem {contma} produtos custando mais de R$1000.00
O produto mais barato foi {nmenor} que custa R${pmenor:.2f}''')
