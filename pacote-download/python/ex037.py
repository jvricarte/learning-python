num = int(input('Digite um número inteiro: '))
print('''Escolha uma das opções para conversão:
[1] Converter para binário
[2] Converter para octal
[3] Converter para hexadecimal''')
op = int(input('Sua opção: '))
if op == 1:
    print('O número {} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} convertido para hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
