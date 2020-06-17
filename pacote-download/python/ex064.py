cont = soma = 0
num = int(input('Digite um número: '))
while num != 999:
    cont = cont + 1
    soma = soma + num
    num = int(input('Digite um número: '))
print('Você digitou {} números e a soma deles é {}'.format(cont, soma))
