from datetime import date

print('-=' * 10, 'ANO BISSEXTO', '-=' * 10)
ano = int(input('Digite um ano. Se for o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # o ano tem que ser divisível por 4, não divisível por 100 e divisível por 400
    print(f'O ano de {ano} é BISSEXTO!')
else:
    print(f'O ano de {ano} não é BISSEXTO!')
