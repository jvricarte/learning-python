from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    cont = i

    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

# programa principal
contador(1, 10, 1)
contador(10, 0, 2)

ini = int(input('Contar a partir do número: '))
fim = int(input(f'Contar do número {ini} até o número: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)
