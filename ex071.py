#Crie um programa que simule o funcionamento de
#um caixa eletrônico. No início, pergunte ao 
#usuário qual será o valor a ser sacado (número
#inteiro) e o programa vai informar quantas 
#cédulas de cada valor serão entregues. OBS:
    #considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print ("CAIXA ELETRÔNICO")

valor = int(input("Quanto deseja sacar? R$"))
montante = valor
cedulas = 50
total = 0

while True:
    if montante >= cedulas:
        montante -= cedulas
        total += 1
    else:
        if total  >0:
            print (f"Total de {total} cédulas de R${cedulas}")
        #ifs separados são cadeias diferentes mesmo que na mesma linha vertical
        if cedulas == 50:
            cedulas = 20
        #elif junta uma cadeia de if
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        #zerar valor de cédulas para contar a próxima
        total = 0
        if montante == 0:
            break

print ("Obrigado por usar este banco. Volte sempre!")

