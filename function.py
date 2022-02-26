print("============FUNÇÕES===========")
#def dobro (numero):
#    return numero * 2
#print(dobro (5))

#Variável local
def multiplica (num1, num2):
    numero= num1 * num2
    return numero #numero é uma variável local
print(multiplica(20,5))

n1 = 16 #Variáveis globais
n2 = 4
def divisao ():
    return n1/n2
print(divisao())