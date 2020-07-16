from random import randint

def sorteia(lista):
    for cont in range(0, 5):
        lista.append(randint(0, 10))

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares é igual a {soma}')


# programa principal
numeros = list()
sorteia(numeros)
print(numeros)
somapar(numeros)