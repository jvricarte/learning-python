l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 and l2 == l3:
        print('TRIÂNGULO EQUILÁTERO')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('TRIÂNGULO ISÓSCELES')
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print('TRIÂNGULO ESCALENO')
else:
    print('TRIÂNGULO INEXISTENTE')
