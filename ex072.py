extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quartoze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')
núm = int(input('Escreva um número entre 0 e 20: '))

while núm not in range(0,21):
    núm = int(input('Erro, tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[núm]}')
