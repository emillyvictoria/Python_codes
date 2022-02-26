numeros = range(10)
print(numeros)
#for num in range(1,11):
#    print(num)
for num in numeros:
    num = num+1
    print(f'Tabuada de {num}:')
    for multiplicador in numeros:
        print((multiplicador+1)*num)