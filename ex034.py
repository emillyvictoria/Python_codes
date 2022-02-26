print ('-='*10, 'AUMENTO DE SALÁRIO'.upper(), '-='*10)
sal = float(input('Digite o seu salário: '))
if sal >= 1250.0:
    sal = sal + sal * (10/100)
    print(f'Você recebeu um aumento de 10%, o seu novo salário é {sal}!')
else:
    sal = sal + sal * (15/100)
    print(f'Você recebeu um aumento de 15%, o seu novo salário é {sal}!')