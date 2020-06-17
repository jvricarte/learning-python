s = float(input('Qual o salário do funcionário? '))
if s > 1250:
    print('O aumento será de 10% e o valor final será R${}'. format((10/100 * s) + s))
else:
    print('O aumento será de 15% e o valor final será R${}'.format((15/100 * s) + s))
