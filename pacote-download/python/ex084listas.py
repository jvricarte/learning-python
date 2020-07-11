temp = list()
princ = list()
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    res = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if res == 'N':
        break
print(f'O total de pessoas cadastradas foi de {len(princ)}')
print(f'O maior peso foi de {mai}Kg. Peso de  ', end='')
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]')
