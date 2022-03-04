num = 1

while True:
    tab = int(input('Deseja ver a tabuada de qual valor? '))
    print('-'*20)
    if tab < 0:
        break
    while num <= 10:
        resul = tab*num
        print(f'{tab} x {num} = {resul}')
        num += 1
    num = 1
    print('-'*20)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
