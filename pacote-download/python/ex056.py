somaidade = 0
mediaidade = 0
maioridadeH = 0
nomevelho = ''
totmulher20 = 0
#Colhendo dados
for p in range(1, 5):
    print('----- {}ª Pessoa -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    # Somando as idades
    somaidade = somaidade + idade
    # Identificando o nome do homem mais velho
    if p == 1 and sexo in 'Mm':
        maioridadeH = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadeH:
        maioridadeH = idade
        nomevelho = nome
    # Quantidade de mulheres com menos de 20 anos
    if sexo in 'fF' and idade < 20:
        totmulher20 = totmulher20 + 1
# Calculando a média das idades
mediaidade = somaidade / 4
#Saída de dados
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeH, nomevelho))
print('Ao todo há {} mulheres com menos de 20 anos'.format(totmulher20))
