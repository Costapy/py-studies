from random import randint

print('-='*15)
print('Vamos Jogar Para Ou Ímpar')
soma = 0
cont = 0

while True:
    print('-=' * 15)
    jogador = int(input('Escolha um valor: '))
    escolha = str(input('Para ou ímpar [P/I]? ')).upper().strip()[0]
    computador = randint(0,10)
    soma = jogador + computador
    vencedor = ''
    print('-'*30)
    if soma%2 == 0:
        vencedor = 'P'
        print(f'Você jogou {jogador} e o computador {computador}. O total foi igual a {soma}, ou seja, é PAR!')
    else:
        vencedor = 'I'
        print(f'Você jogou {jogador} e o computador {computador}. O total foi igual a {soma}, ou seja, é ímpar!')
    print('-'*30)
    if escolha == vencedor:
        print('Você venceu!')
        cont += 1
        print('Vamos jogar novamente...')
    else:
        print('Você perdeu!')
        break
print('-='*15)
print(f'GAME OVER! Você venceu {cont} vezes.')
