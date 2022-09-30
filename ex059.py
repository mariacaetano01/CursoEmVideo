#Crie um programa que leia dois valores e mostre um menu na tela:
    # [ 1 ] somar
    # [ 2 ] multiplicar
    # [ 3 ] maior
    # [ 4 ] novos números
    # [ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))
op = 0
print (" ")

while op != 5:
    print ("[ 1 ] Somar")
    print ("[ 2 ] Multiplicar")
    print ("[ 3 ] Maior")
    print ("[ 4 ] Novos números")
    print ("[ 5 ] Sair")
    print (" ")
    op = int(input("Digite a operação que você precisa: "))
    print (" ")

    if op == 1:
        soma = n1+n2
        print (f"Soma = {soma}")
        print (" ")
    elif op == 2:
        multi = n1*n2
        print (f"Multiplicação = {multi}")
        print (" ")
    elif op == 3:
        if n1 > n2:
            print (f"O maior número é {n1}")
            print (" ")
        else:
            print (f"O maior número é {n2}")
            print (" ")
    elif op == 4:
        print ("Informe os números novamente:")
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite outro valor: "))
        print (" ")
    elif op == 5:
        print ("Finalizando...")
        sleep (2)
        print ("Programa encerrado.")
        break
    else:
        print ("Opção inválida, digite novamente!")

