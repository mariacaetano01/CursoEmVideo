#Refaça o DESAFIO 9, mostrando a tabuada de
#um número que o usuário escolher, só que agora
# utilizando um laço for.
    #Faça um programa que leia um número inteiro qualquer 
    #e mostre na tela a sua tabuada

    # print ("Vamos aprender a tabuada?")
    # n = int(input('Digite a tabuada que quer saber: '))
    # print (f'1 x {n} = {1*n}')
    # print (f'2 x {n} = {2*n}')
    # print (f'3 x {n} = {3*n}')
    # print (f'4 x {n} = {4*n}')
    # print (f'5 x {n} = {5*n}')
    # print (f'6 x {n} = {6*n}')
    # print (f'7 x {n} = {7*n}')
    # print (f'8 x {n} = {8*n}')
    # print (f'9 x {n} = {9*n}')
    # print (f'10 x {n} = {10*n}')

num = int(input('Qual número quer saber a tabuada? '))
for contador in range (1,11):
    print (f'{contador} x {num} = {contador*num}')

print ("Que bom que pude ajudar ♥")