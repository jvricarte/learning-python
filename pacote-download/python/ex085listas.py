numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input('Digite um número: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
        numeros[0].sort()
    else:
        numeros[1].append(valor)
        numeros[1].sort()
print(f'A lista de números pares é {numeros[0]}')
print(f'A lista de números ímpares é {numeros[1]}')
