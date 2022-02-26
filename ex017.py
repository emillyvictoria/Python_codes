import math
#print ('='*8, 'Catetos e Hipotenusa', '='*8)
#ops = float (input('Digite o valor do cateto oposto do triângulo: '))
#adj = float (input('Digite o valor do cateto adjacente do triângulo: '))
#hipo = (ops**2) + (adj**2)
#x = math.sqrt(hipo)
#print(f'O comprimento da hipotenusa é igual a {x}')

#ou

print ('='*8, 'Catetos e Hipotenusa', '='*8)
ops = float (input('Digite o valor do cateto oposto do triângulo: '))
adj = float (input('Digite o valor do cateto adjacente do triângulo: '))
hipo = math.hypot(ops, adj)
print(f'O comprimento da hipotenusa é igual a {hipo.__round__(3)}')