#Desafio 10
'''
Faça um programa que leia um número inteiro e
mostre na tela o seu sucessor e o seu
antecessor
'''

print ("Qual o antecessor e o sucessor?")
valor = int(input("Digite um número inteiro: "))
a = valor - 1
s = valor + 1
print (f'O antecessor de {valor} é {a} e o sucessor é {s}')