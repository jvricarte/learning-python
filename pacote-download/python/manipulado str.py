#MANIPULANDO TEXTO
'''frase[9] identifica o caracter 9, o décimo caracter
frase[9:13] seleciona do caracter 9 ao 12
frase[9:13:2] do 9 ao 12 pulando de 2 em 2
frase[:5] do 0 ao 4
frase[15:] do 15 ao final
frase[9::3] do 9 ao fim pulando de 3 em 3
len(frase) comprimento da frase
frase.count(o) conta qnts letras o tem na string
frase.count(o, 0, 13) conta qnts o tem do 0 ao 12 caracter
frase.find(deo) localiza em que momento começa o deo
'curso' in frase verificar se existe a palavra curso na frase / retorna true ou false
frase.replace('python', 'android') onde tiver python vai ser trocado por android
frase.upper() o q já for maiusculo mantem, o q não for o torna
frase.lower() o que já for minusculo mantem, oq não for o torna
frase.captalize() torna maiuscula somente a letra q inicia a frase
frase.title() torna maiuscula as primeiras letras de cada palavra da frase
frase.strip() ignora todos os espaços excedentes à esquerda e à direita
frase.rstrip() ignora espaços excedentes somente a direita
frase.lstrip() ignora espaços excedentes somente a esquerda
frase.split() divide a string onde tiver espaço entre as palavras gerando uma lista
'-'.join(frase) junta a split com o "-"
'''
