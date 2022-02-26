from random import shuffle
print ('='*8, 'APRESENTAÇÃO', '='*8)
p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Terceiro aluno: ')
q = input('Quarto aluno: ')
lista = [p, s, t, q]
shuffle(lista)
print(f'A ordem de apresentação será:\n {lista}')