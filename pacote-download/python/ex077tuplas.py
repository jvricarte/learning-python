palavras = ('programar', 'gratis', 'curso', 'tecnologia', 'inteligencia')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')