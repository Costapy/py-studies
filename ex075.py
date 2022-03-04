núm = (int(input('Digite o primeiro número: ')),
       int(input('Digite o primeiro número: ')),
       int(input('Digite o primeiro número: ')),
       int(input('Digite o primeiro número: ')))

print(f'Você digitou os valores {núm}')
print(f'O número 9 aparece {núm.count(9)} vezes')
if 3 in núm:
       print(f'O número 3 foi digitado na {núm.index(3)+1}ª posição')
else:
       print('O número 3 não foi digitado em nenhuma posição')
print('Os números pares digitados foram ', end='')
for v in núm:
       if v % 2 == 0:
              print(f'{v} ',end='')
