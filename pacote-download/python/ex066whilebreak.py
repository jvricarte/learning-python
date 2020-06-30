s = cont = 0
while True:
    n = int(input('Digite um número inteiro (999 para parar): '))
    if n == 999:
        break
    cont = cont + 1
    s = s + n
print(f'A soma dos {cont} valores é de {s}')
