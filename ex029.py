print ('-='*10, 'RADAR DE VELOCIDADE', '-='*10)
v = int(input('Qual a velocidade que você estava andando na cidade? '))
if v >= 80.0:
    multa = (v-80)*7
    print(f'Você excedeu o limite de velocidade da pista que é de 80Km/h!\nPor conta disso, você receberá uma multa de {multa} reais!')
else:
    print(f'Você está dentro do limite de velocidade, muito bem!')