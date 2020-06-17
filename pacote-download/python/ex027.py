n = str(input('Digite o seu nome: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é {} e o último é {}'.format(nome[0], nome[len(nome)-1]))
