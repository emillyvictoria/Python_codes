print('='*8, 'Aluguel de carros', '='*8)
dia = int (input('Por quantos dias o carro foi alugado? '))
km = float (input('Quantos km foram rodados nesse período? '))
calculo = 60*dia + 0.15*km
print('O valor total a ser pago pelo o aluguel do carro é de R${:.2f}'.format(calculo))
