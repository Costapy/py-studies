from random import randint

sorteio = (randint(1,10), randint(1,10), randint(1,10),
           randint(1,10), randint(1,10))

print('Os números sorteados foram: ', end='')
for núm in sorteio:
    print(f'{núm} ', end='')
print(f'\nO maior valor sorteado foi o {max(sorteio)}')
print(f'O menor valor sorteado foi o {min(sorteio)}')
