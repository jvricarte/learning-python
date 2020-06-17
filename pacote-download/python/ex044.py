print('=' * 10, ' LOJAS AMERICANAS ', '=' * 10)
preco = float(input('Valor da compra: '))
print('=' * 40)
print('''FORMAS DE PAGAMENTO
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('O valor total com desconto de 10% será de R$ {:.2f}'.format(preco - 10 / 100 * preco))
elif opcao == 2:
    print('O valor total com 5% de desconto será de R$ {:.2f}'.format(preco - 5 / 100 * preco))
elif opcao == 3:
    print('O valor final será de duas parcelas de R$ {:.2f}'.format(preco / 2))
elif opcao == 4:
    parc = int(input('Quantidade de parcelas desejadas: '))
    print('O valor final será de {} parcelas de R$ {:.2f}'.format(parc, (preco + 20 / 100 * preco) / parc))
else:
    print('Opção inválida')
