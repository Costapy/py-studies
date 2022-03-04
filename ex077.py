palavras = ('aprender', 'programar', 'linguagem', 'python',
           'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
           'mercado', 'programador', 'futuro')

for v in palavras:
    print(f'\nNa palavra {v} temos as vogais ', end='')
    for c in v:
        if c.lower() in 'aeiou':
            print(f'{c} ', end='')
