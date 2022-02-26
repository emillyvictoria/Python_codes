print('========== Descontos =========')
prod = float (input('Qual é o valor do produto? '))
desc = (prod * 5) / 100
final = prod - desc
print('Você recebeu 5% de desconto (R${:.1f})!\nCom isso, o valor final do seu produto é de R${:.2f}'.format(desc, final))