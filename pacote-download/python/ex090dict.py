cad = dict()
cad['nome'] = str(input('Digite o seu nome: '))
cad['media'] = float(input(f'Média de {cad["nome"]}: '))
if cad['media'] >= 7:
    cad['resultado'] = 'Aprovado'
else:
    cad['res'] = 'Reprovado'
for k, v in cad.items():
    print(f'{k} é igual a {v}')
