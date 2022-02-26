#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {:20}!'.format(nome)) #digita o nome com 20 caracteres depois dele
#print('Prazer em te conhecer {:>20}!'.format(nome)) #nome alhinhado a direta em 20 caracteres
#print('Prazer em te conhecer {:^20}!'.format(nome)) #centralizar o nome
#print('Prazer em te conhecer {:=^20}!'.format(nome)) #com iguais em volta

n1 = int (input ('Digite um valor: '))
n2 = int (input ('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1**n2

print('A soma é igual a: {} \n o produto é {} \n a divisão é {:.3f}'.format(s, m, d), end =' ')
print ('\n A divisão inteira é: {} \n A potência {}'.format(di,e))