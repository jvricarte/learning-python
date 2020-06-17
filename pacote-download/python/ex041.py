from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('--- CONFEDERAÇÃO NACIONAL DE NATAÇÃO ---')
print('=' * 40)
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('CLASSIFICAÇÃO: Mirim')
elif idade <= 14:
    print('CLASSIFICAÇÃO: Infantil')
elif idade <= 19:
    print('CLASSIFICAÇÃO: Júnior')
elif idade <= 25:
    print('CLASSIFICAÇÃO: Sênior')
elif idade > 25:
    print('CLASSIFICAÇÃO: Master')
