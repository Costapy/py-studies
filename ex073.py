times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro',
         'Flamengo', 'Vasco', 'Chapecoense', 'Atlético-MG', 'Botafogo',
         'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-='*25)
print(times)
print('-='*25)
print(f'Os 5 primeiros são: {times[:5]}')
print('-='*25)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*25)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*25)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')
