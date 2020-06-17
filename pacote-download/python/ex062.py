print('GERADOR DE PA')
print('=-' * 10)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termo = a1
total = 0
cont = 1
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo = termo + r
        cont = cont + 1
    print('Acabou!')
    mais = int(input('Quer mais quantos termos? '))
print('FIM')
print('O total de termos mostrados foi de {}'.format(total))
