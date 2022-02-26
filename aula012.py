nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Emilly':
    print('Que nome lindo!')
elif nome == 'João' or nome == 'Maria' or nome == 'Alice':
    print('Que nome normal k')
else:
    print(f'Bom dia, {nome}!')