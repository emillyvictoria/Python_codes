print('='*8, 'Reajuste salarial', '='*8)
sal = float (input('Qual é o seu salário atual? '))
aum = sal + (sal*15/100)
print('Você recebeu um aumento de 15%!\nCom isso, o seu novo salário é R${:.2f}'.format(aum))