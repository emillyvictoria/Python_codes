from math import trunc
print ('='*8, 'Quebrando um número', '='*8)
real = float(input('Digite um número real qualquer: '))
inteiro = trunc(real)
print(f'O número {real} tem a parte inteira {inteiro}')