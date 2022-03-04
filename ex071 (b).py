print('='*20)
print('{:^20}'.format('BANCO COSTA'))
print('='*20)
valor = int(input('Qual a quantia que você deseja sacar? '))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        print(f'Total de {totalced} de cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
    if total == 0:
        break
print('='*20)
print('FIM DO PROGRAMA')
