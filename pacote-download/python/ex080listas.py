lista = []
for c in range(0, 5):
    n = int(input('Digite um número: '))
    # Se for o primeiro valor ou se o valor for maior que o ultimo
    # Então adicionamos na lista
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionando no final da lista')
    else:
        pos = 0
        # Varrendo o vetor do inicio ao fim
        while pos < len(lista):
            # Inserir o número na posição em que o número contido for menor ou igual...
            # ... ao número que estamos inserindo
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionando na posição {pos} da lista.')
                break
            # Possibilitando a verificação de cada posição...
            # ... uma após a outra
            pos += 1
print(f'Os valores digitados em ordem foram {lista}')
