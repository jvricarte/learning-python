print('-' * 30)
print('CADASTRO DE PESSOAS')
print('-' * 30)
total18 = 0
totalman = 0
totalw = 0
while True:
    age = int(input('Idade: '))
    sex = ' '
    while sex not in 'FM':
        sex = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if age >= 18:
        total18 = total18 + 1
    if sex in 'M':
        totalman = totalman + 1
    if sex in 'F' and age >= 20:
        totalw = totalw + 1
    loop = ''
    while loop != 1 and loop != 0:
        loop = int(input('[1] para continuar [0] para parar: '))
    print('-' * 30)
    if loop == 0:
        break
print(f'''
O total de pessoas com mais de 18 anos é {total18}
O total de homens cadastrados é {totalman}
E o total de mulheres com mais de 20 anos é {totalw}''')
