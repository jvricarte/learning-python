lista = []
lista.append(str(input('Digite uma expressão matemática: ')))
right = lista.count(')')
left = lista.count('(')
if right == left:
    print('Expressão válida')
else:
    print('Expressão inválida')
