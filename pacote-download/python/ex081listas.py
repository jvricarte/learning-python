lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    res = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if res == 'N':
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('Não encontrei o valor 5 na lista!')
