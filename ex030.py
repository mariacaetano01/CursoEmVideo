'''
Crie um programa que leia um número
 inteiro e mostre na tela se ele é 
 PAR ou ÍMPAR.
'''

print ("Par ou impar?")
num = int(input('Digite um numero: '))

divisao = num % 2

if divisao == 0:
    print (f'O numero {num} é PAR')
else:
    print (f'O numero {num} é IMPAR')