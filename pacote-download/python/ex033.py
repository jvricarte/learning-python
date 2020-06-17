a = int(input('Digite um valor inteiro: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))
#verificando o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi o {} e o menor foi o {}'.format(maior, menor))
