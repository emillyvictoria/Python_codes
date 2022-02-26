import numpy as np
array2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(type(array2d))
print(array2d)
print(array2d.shape) #dimensão da array
  #Slicing
print(array2d[0,1])
  #Operadores
print('MULTIPLICAÇÃO: ',array2d*2)
print('DIVISÃO: ',array2d/2)
print('EXPONENCIAÇÃO: ',array2d**3)
print('RAIZ:',np.sqrt(array2d)) #raiz quadrada
print('LOG: ',np.log(array2d))
print('SENO: ', np.sin(array2d))
  #Métodos de criação
print(np.ones((3,3)))# ones ou zeros
print(np.eye(4))# eye(matriz identidade --> diagonal 1)
print(np.random.random((5,4))) #arrays randômicas// o '*' serve para definir um parametro para a array
print(np.arange(10)) #arange faz uma lista com 10 valores
print(np.arange(10,100,5)) #arange faz uma lista de 10 a 100 pulando de 5 em 5 (intervalo)
array = np.linspace(1,10,10) #linspace faz uma array de 1 a 10 com 10 valores
print(array)
print(array.reshape(5,2)) #muda a forma da array existe (OBS: os parametros exigidos tem que fazer sentido com o input)
  #Operações entre matrizes
array_1 = np.arange(1,100,5)
array_1 = array_1.reshape(4,5)
print(array_1)
array_2= np.arange(101,150,5)
array_2 = array_2.reshape(5,2)
print(array_2)

array_dot = np.dot(array_1,array_2) #multiplicação de matrizes
print(array_dot)
print(array_dot.shape) #dps da multi ela adquire o formato 4x2

  #Estatística
array2d = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array2d.mean()) #calcula a média da array
print(array2d[0].mean()) #calcula a média  de somente uma linha da array
print(array2d.std()) #calcula o desvio padrão da array
