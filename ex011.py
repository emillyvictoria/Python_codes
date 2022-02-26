print('======= Pinta fácil =======')
la = float (input('Qual é a largura da parede em metros? '))
al = float (input('Qual é a altura da parede em metros? '))
area = la * al
tinta = area / 2
print('É necessário {:.1f} litros de tinta para pintar uma área de {:.1f}m de parede!'.format(tinta, area))