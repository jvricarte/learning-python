from math import sqrt
o = float(input('Digite o comprimento do cateto oposto: '))
a = float(input('Digite o comprimento do cateto adjacente: '))
h = sqrt(o ** 2 + a ** 2)
print('O comprimento da hipotenusa é {:.1f}'.format(h))

'''Para evitar a importação, pode-se elevar a soma dos quadrados a 1/2 extraindo assim a raiz
nesse caso não pode-se esquecer de evidenciar a soma dos quadrados com parenteses para forçar a prioriade
do cálculo
ATENÇÃO: pode-se usar math.hypot(o, a)
