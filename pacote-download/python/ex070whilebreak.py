total = 0
total1000 = 0
cont = 0
smallername = ' '
smallerprice = 0
while True:
    #Contabilizando o número de laços do loop
    cont = cont + 1
    #Colhendo os dados
    product = str(input('Produto: '))
    price = float(input('Preço: R$'))
    total = total + price
    #Verificar se é o primeiro laço
    if cont == 1:
        #Os dados coletados no primeiro laço são considerados os do menor preço
        smallername = product
        smallerprice = price
    #Se não for o primeiro laço, isto é, se for os demais, então:
    else:
        #Se o preço dos demais laços for menor do que o que foi considerado no laço anterior
        #Então o menor passa a ser o do laço em questão
        if price < smallerprice:
            smallerprice = price
            smallername = product
    #Se o preço for maior que mil reais então contabilizamos mais 1 à variável
    if price > 1000:
        total1000 = total1000 + 1
    loop2 = ' '
    #Um segundo loop é criado para garantir que o usuário digite corretamente
    while loop2 not in 'SN':
        loop2 = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    #Condição de quebra do loop
    if loop2 == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'''O total da compra foi de {total}
{total1000} dos produtos são acima de 1000 reais
O produto mais barato foi o {smallername} que custou {smallerprice:.2f}''')


#ATENÇÃO: UMA VEZ QUE HÁ DOIS BLOCOS DE CONDICIONAIS IGUAIS, EU POSSO OMITIR O ULTIMO DELES DESDE QUE
#CONDICIONE COM O 'OR' NO PRIMEIRO AS DUAS SITUAÇÕES