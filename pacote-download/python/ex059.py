from time import sleep
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
option = 0
while option != 5:
    print('''
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    option = int(input('Digite a sua opção: '))
    if option == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif option == 2:
        multi = n1 * n2
        print('A multiplicação de {} por {} é igual a {}'.format(n1, n2, multi))
    elif option == 3:
        if n1 > n2:
            print('O maior número entre os digitados é {}'.format(n1))
        elif n2 > n1:
            print('O maior número entre os digitados é {}'.format(n2))
    elif option == 4:
        print('Você selecionou a opção de escolher outros números')
        n1 = int(input('Digite o primeiro novo número: '))
        n2 = int(input('Agora digite o segundo: '))
    elif option == 5:
        print('Saindo do programa conforme solicitado...')
    else:
        print('OPÇÃO INVÁLIDA! Tente novamente.')
    print('=-' * 15)
    sleep(1)
print('Fim do programa. Volte sempre!')
