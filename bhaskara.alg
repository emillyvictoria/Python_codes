algoritmo "semnome"
// Função :
// Autor :
// Data : 12/09/2021
// Seção de Declarações 
var
a, b, c, delta, x1, x2: real
inicio
escreva ("Digite um valor para a: ")
leia (a)
escreva ("Digite um valor para b: ")
leia (b)
escreva ("Digite um valor para c: ")
leia (c)
escreval ("Sua função de 2° grau é igual a: ", a, "^2x", b, "x", c, "=0")
delta <- b^2 - 4*a*c
escreval ("O valor de delta é: ", delta)
x1 <- (-b + RaizQ (delta))/2*a
escreval ("O valor de x'= ",x1)
x2 <- (-b - RaizQ (delta))/2*a
escreval ("O valor de x''= ",x2)
fimalgoritmo
