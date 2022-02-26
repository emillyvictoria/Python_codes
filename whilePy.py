contador = 0
#while contador < 10:
    #print(f'Estou dentro do while! contador = {contador}')
    #contador +=1 #contador = contador + 1
#else:
#    print(f'Estou fora do while porque contador = {contador}')

#BREAK
while contador < 10:
   if contador == 5:
        break #para no 5
   print(contador)
   contador += 1
#CONTINUE
while contador < 10:
    if contador == 5:
        contador += 1
        continue #pula o 5 e continua
    print(contador)
    contador += 1