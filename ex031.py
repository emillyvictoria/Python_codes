print ('-='*10, 'passagem'.upper(), '-='*10)
d = int (input('Qual a distância da sua viagem em Km? '))
if d <= 200:
    p = d*0.5
    print(f'A sua viagem não é muito distante, por isso, o preço da sua passagem é {p} reais')
else:
    p2 = d*0.45
    print(f'A sua viagem é bem longa, por isso, o preço da sua passagem é {p2} reais')