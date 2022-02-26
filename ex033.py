print('-=' * 10, 'MAIOR E MENOR', '-=' * 10)
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
menor = n1
if n2<n1 or n2<n3:
    menor = n2
if n3<n1 or n3<n2:
    menor = n3

maior = n1
if n2>n1 or n2>n3:
    maior = n2
if n3>n1 or n3>n1:
    maior = n3
print(f'O menor número digitado foi: {menor} ')
print(f'O maior número digitado foi: {maior} ')
