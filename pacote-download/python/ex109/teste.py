import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p, 10, True)}')
print(f'Diminuindo em 10%, temos R${moeda.diminuir(p, 10, True)}')
