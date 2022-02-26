import random

print ('='*8, 'SORTEIO', '='*8)
p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Terceiro aluno: ')
q = input('Quarto aluno: ')
lista = [p, s, t, q]
sorteio = random.choice(lista)
print(f'O aluno (a) escolhido foi: {sorteio}!')