#Elabore um programa que calcule o valor a ser pago
#por um produto, considerando o seu preço normal e
# condição de pagamento:
    # à vista dinheiro/cheque: 10% de desconto
    # à vista no cartão: 5% de desconto
    # em até 2x no cartão: preço formal 
    # 3x ou mais no cartão: 20% de juros

from time import sleep

print ('VERIFICADOR DE PREÇO COM DESCONTO/JUROS')
preco = float(input("Preço do produto: "))
print (' ')
print ('Escolha a forma de pagamento:')
print ('[ 1 ] à vista, dinheiro')
print ('[ 2 ] à vista, cheque')
print ('[ 3 ] à vista, no cartão')
print ('[ 4 ] em 2x, no cartão')
print ('[ 5 ] em 3x ou mais, no cartão')
pgmto = int(input('Digite aqui a opção: '))
print (' ')

desconto_d = preco - (preco*0.1)
desconto_c = preco - (preco*0.05)
juro = preco * 1.2

if pgmto == 1 or pgmto == 2:
    print (f"O valor a ser pago é de R${round(desconto_d,2)}")
elif pgmto == 3:
    print (f'O valor a ser pago é de R${round(desconto_c,2)}')
elif pgmto == 4:
    print (f"O valopr a ser pago é de R${preco}")
elif pgmto == 5:
    print (f"O valor a ser pago é de R${round(juro,2)}")
else:
    print ('Opção inválida, refaça a operação')
    sleep (2)
    print ('Escolha a forma de pagamento:')
    print ('[ 1 ] à vista, dinheiro')
    print ('[ 2 ] à vista, cheque')
    print ('[ 3 ] à vista, no cartão')
    print ('[ 4 ] em 2x, no cartão')
    print ('[ 5 ] em 3x ou mais, no cartão')
    pgmto = int(input('Digite aqui a opção: '))
    print (" ")
    if pgmto == 1 or pgmto == 2:
        print (f"O valor a ser pago é de R${round(desconto_d,2)}")
    elif pgmto == 3:
     print (f'O valor a ser pago é de R${round(desconto_c,2)}')
    elif pgmto == 4:
        print (f"O valopr a ser pago é de R${preco}")
    elif pgmto == 5:
        print (f"O valor a ser pago é de R${round(juro,2)}")
    else:
        print ('Opção inválida, operação será cancelada!')
