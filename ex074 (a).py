from random import sample

lista = sample([1,2,3,4,5,6,7,8,9,10], k=5)
maior = menor = 0

print(f'Os valores sorteados foram: {lista}')
for pos, núm in enumerate(lista):
    if pos == 0:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
print(f'''O maior número foi o {maior}
O menor número foi o {menor}''')
