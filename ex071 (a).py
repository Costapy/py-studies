print('='*20)
print('{:^20}'.format('BANCO COSTA'))
print('='*20)
valor = int(input('Qual valor deseja sacar? '))
total = cont50 = cont20 = cont10 = cont1 = 0

while total < valor:
    while True:
        if total + 50 > valor:
            break
        total += 50
        cont50 += 1
    while True:
        if total + 20 > valor:
            break
        total += 20
        cont20 += 1
    while True:
        if total + 10 > valor:
            break
        total += 10
        cont10 += 1
    while True:
        if total + 1 > valor:
            break
        total += 1
        cont1 += 1
print(f'''Total de {cont50} cédulas de R$50
Total de {cont20} cédulas de R$20
Total de {cont10} cédulas de R$10
Total de {cont1} cédulas de R$1''')
print('='*20)
print('FIM DO PROGRAMA')
