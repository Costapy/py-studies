num = []

for c in range(0, 5):
    val = int(input('Digite um valor: '))
    if c == 0 or val > num[len(num)-1]:
        num.append(val)
        print('Adicionado no final...')
    else:
        pos = 0
        while pos < len(num):
            if val <= num[pos]:
                num.insert(pos, val)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print('-='*30)
print(f'Os valores da lista são: {num}')
