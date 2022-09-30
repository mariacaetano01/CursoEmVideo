#Escreva um programa que leia dois números inteiros 
# compare-os. mostrando na tela uma mensagem:
    #O primeiro valor é maior
    #O segundo valor é maior
    #Não existe valor maior, os dois são iguais

from time import sleep

print ('COMPARANDO DOIS INTEIROS')
print("Digite, a seguir, dois números inteiros:")
num1 = int(input("Digite aqui: "))
num2 = int(input("Digite aqui: "))
print ("Agora eu direi se um é maior que outro...")

sleep (5)

if num1 > num2:
    print (f'{num1} é maior que {num2}')
elif num1 < num2:
    print (f'{num2} é maior que {num1}')
else:
    print (f'Os números são iguais')

print ("OBRIGADO POR USAR ESTE PROGRAMA!")