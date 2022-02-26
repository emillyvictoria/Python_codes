print ('='*10, 'NOME SILVA', '='*10)
nome = input('Digite o seu nome: ').strip()
if  'SILVA' in nome.upper():
    print('Você possui Silva no seu nome!')
else:
    print('Você não possui Silva no seu nome :(')