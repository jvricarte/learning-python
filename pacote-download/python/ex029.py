print('='*15, 'RADAR', '='*15)
v = float(input('Em que velocidade em km/h o carro está? '))
print('O carro está a uma velocidade de {} km/h'.format(v))
if v > 80:
    print('Você foi multado no valor de R${:.2f}'.format((v - 80) * 7))
print('='* 5, 'Obrigado, tenha um bom dia', '='*5)