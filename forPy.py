#Testes com "for"
Brasilia = 'Taguatinga', 'Guará', 'Bandeirante', 'Cruzeiro', 'Plano Piloto', 'Águas Claras'
for cidade in Brasilia:
    print(cidade)
for letra in 'Guará':
    print(letra)

lista = [1,2,3,4,5,6,7,8,9]
for num in lista:
    print(f'{num} ao quadrado = {num**2}')
for i in lista:
    if i > 5:
        print(i)


for i in lista:
    if i % 2 == 0:
        lista_par = [].append(i)
        print(lista_par)
    else:
        lista_impar = []
        print((lista_impar.append(i)))
