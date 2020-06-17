n1 = int(input('Digite um número para calcular o seu fatorial: '))
cont = n1
print('Calculando {}! ... '.format(n1))
f = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f = f * cont
    cont = cont - 1
print(f)

# Existe um módulo para calcular fatorial