print('='*10, 'viagens.com', '='*10)
d = float(input('Qual a distância em km da viagem que você deseja fazer? '))
print('Calculando...')
if d <= 200:
    print('O preço da sua passagem é de R${:.2f}'.format(d * 0.5))
else:
    print('O valor da sua passagem é de R${:.2f}'.format(d * 0.45))
