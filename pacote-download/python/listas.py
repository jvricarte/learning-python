'''
nome_da_lista.append(valor) adiciona elemento a lista

nome_da_lista.sort() coloca em ordem

nome_da_lista.sort(reverse=True) coloca em ordem decrescente

len(nome da lista) indica quantos elementos tem na lista

nome_da_lista.insert(posição, valor) insere valores em quaisquer posições que já existem na lista

nome_da_lista.pop(indice da posição) sem parâmetro remove o ultimo elemento da lista, mas
podemos colocar o indice como parâmetro

nome_da_lista.remove(valor) remove o primeiro valor indicado, da esquerda pra direita

'''
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')

'''
ATENÇÃO PARA UMA PECULIARIDADE
a = [1, 2, 3, 4]
b = a
uma vez que b recebe a, temos duas listas identicas e intimamente ligadas uma a outra
isto quer dizer que qualquer mudança que eu fizer numa lista irá alterar também a outra

uma forma de criar uma cópia de uma lista sem haja essa ligação entre elas é a seguinte:
b = a[:]
dessa maneira podemos alterar elementos em b sem alterar em a
'''
