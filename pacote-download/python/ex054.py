from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Ano do nascimento: '))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1 #ou totmaior += 1
    else:
        totmenor = totmenor + 1 #ou totmenor += 1
print('Ao todo tivemos {} pessoas maiores e {} menores de idade'.format(totmaior, totmenor))
