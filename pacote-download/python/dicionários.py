pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['sexo']
pessoas['nome'] = 'Leandro'
for k, v in pessoas.items():
    print(f'{k} = {v}')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federatia: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
print(brasil)
