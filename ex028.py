import random
print ('-='*10, 'Jogo da Adivinhação', '-='*10)
n1 = random.randint(1,5)
n2 = int(input('Tente adivinhar o número que o computador escolheu (de 1 até 5): '))
if n1 == n2:
    print(f'O número que o computador escolheu foi... {n1}\nParabéns você acertou!')
else:
    print(f'O número que o computador escolheu foi... {n1}\nNão foi desa vez!')
