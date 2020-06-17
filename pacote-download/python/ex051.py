a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n = a1 + (10 - 1) * r
for c in range(a1, n + 1, r):
    print(c, end=' -> ')
print('Acabou!')
