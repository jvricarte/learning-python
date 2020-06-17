print('===== BOLETIM UNIPLAN =====')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('=' * 27)
print('Média: {:.2f}'.format(m))
print('=' * 27)
if m < 5.0:
    print('ALUNO REPROVADO!')
elif m >= 5 and m <= 6.9:
    print('ALUNO EM RECUPERAÇÃO!')
elif m > 6.9:
    print('ALUNO APROVADO!')
print('===== BOLETIM UNIPLAN =====')
