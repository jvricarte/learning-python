from time import sleep

def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo')
    print(f'O maior valor informado foi o {maior}')


# programa principal
maior(1, 2, 3, 4, 5, 6)
maior(1, 2, 3, 4)
maior(1, 2)
maior(9)
maior()
