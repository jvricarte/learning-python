print('-=' * 6, '$ EMPRÉSTIMO BANCÁRIO $', '=-' * 6)
v = float(input('Valor do imóvel: '))
prazo = float(input('Prazo do contrato em meses: '))
r = float(input('Renda líquida: '))
parc = v / prazo
if parc > 30 / 100 * r:
    print('Margem excedida')
else:
    print('O valor das parcelas será de R${:.2f} mensais'.format(parc))
