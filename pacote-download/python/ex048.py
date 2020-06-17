cont = 0
soma = 0
for c in range(0, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            soma = soma + c
            cont = cont + 1
            print(c)
print('Soma de todos os {} valores é {}'.format(cont, soma))

#para evitar o primeiro IF podemos fazer: for c in range(1, 501, 2): desta forma sempre retornará
#valores ímpares