soma = cont = 0

while True:
    n = int(input('Digite um número (999 Para parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Você digitou {cont} números e a soma entre ele foi igual a {soma}!')
