soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} valores pares e a soma é {}'.format(cont, soma))
