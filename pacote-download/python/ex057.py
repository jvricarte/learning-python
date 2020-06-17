sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informe o seu sexo [M/F]: ')).strip().upper()[0]
    print('Dados inválidos, tente novamente!')
print('Sexo {} cadastrado com sucesso'.format(sexo))
