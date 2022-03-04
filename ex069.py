print('-'*25)
print('CADASTRO DE PESSOAS')
conth = contm = cont18 = 0

while True:
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    op = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if idade > 18:
        cont18 += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F' and idade < 20:
        contm += 1
    print('-' * 25)
    while op not in 'SN':
        op = str(input('Deseja Continuar? [S/N] ')).upper().strip()[0]
    if op == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {cont18}
Ao todo existem {conth} pessoas do sexo maculino
E temos ao todo {contm} pessoas do sexo feminino com menos de 20 anos''')
