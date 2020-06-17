maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(p)))
    # Verificando o primeiro laço
    if p == 1: # Se for o primeiro laço (a primeira verificação)
        maior = peso # Ao ler o primeiro peso, assumimos como o maior
        menor = peso # Ao mesmo tempo que o menor também
    # Justamente porque se trata da primeira verificação e não há com o que comparar
    else: # Se não, ou seja, nas demais verificações
        if peso > maior: # Se o peso lido for maior que o que foi assumido anteriormente
            maior = peso # Então ele passa a ser o maior
        if peso < menor: # Se for menor que o menor
            menor = peso # então ele passa a ser o menor
print('O maior peso lido foi de {} Kg'.format(maior))
print('O menor peso lido foi de {} Kg'.format(menor))
