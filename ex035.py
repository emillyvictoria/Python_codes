print ('=-'*10, 'Condição de existência de um triângulo'.upper(), '-='*10)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a+b > c and a+c > b and b+c > a:
    print('Esses segmentos podem formar um triângulo!')
else:
    print('Esses segmentos NÃO podem formar um triângulo!')