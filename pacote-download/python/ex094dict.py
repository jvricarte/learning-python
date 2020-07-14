pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        res = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if res in 'SN':
            break
        print('ERRO! Digite apenas S ou N')
    if res == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'fF':
        print(f'{p["nome"]}', end=' ')
print()
print('A lista de pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('< ENCERRADO >')
