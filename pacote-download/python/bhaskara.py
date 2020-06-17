from math import sqrt
from time import sleep
loop = 0
while loop == 0:
    a = int(input('Digite o primeiro termo: '))
    b = int(input('Digite o segundo termo: '))
    c = int(input('Digite o terceiro termo: '))
    d = (b ** 2) - (4 * a * c)
    loop = int(input('Digite [1] para calcular ou [0] para recomeçar: '))
    while loop == 1:
        if d >= 0:
            x1 = (- b + sqrt(d)) / (2 * a)
            x2 = (- b - sqrt(d)) / (2 * a)
            print('As raízes da equação são {:.2f} e {:.2f}'.format(x1, x2))
        else:
            print('As raízes da equação não pertencem ao conjunto dos números reais')
        print('=-' * 30)
        loop = int(input('Digite [1] fazer outro cáculo ou [0] para sair'))
        if loop == 0:
            print('Preparando para sair...')
print('Aguarde')
print('=-' * 20)
sleep(1)
print('Saindo do programa...')
