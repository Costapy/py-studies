valores = []
maior = menor = 0

for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-='*30)
print(f'Você digitou os valores {valores}')

print(f'O maior valor foi {maior} nas posições ', end='')
for pos, num in enumerate(valores):
    if num == maior:
        print(f'{pos}...', end='')
print(f'\nO menor valor foi {menor} nas posições ', end='')
for pos, num in enumerate(valores):
    if num == menor:
        print(f'{pos}...', end='')
