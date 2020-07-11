'''
nome_da_lista.append(valor) adiciona elemento a lista

nome_da_lista.sort() coloca em ordem

nome_da_lista.sort(reverse=True) coloca em ordem decrescente

len(nome da lista) indica quantos elementos tem na lista

nome_da_lista.insert(posição, valor) insere valores em quaisquer posições que já existem na lista

nome_da_lista.pop(indice da posição) sem parâmetro remove o ultimo elemento da lista, mas
podemos colocar o indice como parâmetro

nome_da_lista.remove(valor) remove o primeiro valor indicado, da esquerda pra direita


valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')


ATENÇÃO PARA UMA PECULIARIDADE
a = [1, 2, 3, 4]
b = a
uma vez que b recebe a, temos duas listas identicas e intimamente ligadas uma a outra
isto quer dizer que qualquer mudança que eu fizer numa lista irá alterar também a outra

uma forma de criar uma cópia de uma lista sem haja essa ligação entre elas é a seguinte:
b = a[:]
dessa maneira podemos alterar elementos em b sem alterar em a
'''
# LISTAS DENTRO DE LISTAS

'''teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)'''

galera = list()
dado = list()
totmaior = 0
totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior +=1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade')
