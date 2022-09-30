'''
Faça um programa que leia três números e mostre 
qual é o maior e qual é o menor.
'''

num1 = int(input('Digite um numero qualquer = '))
num2 = int(input('Digite um numero qualquer = '))
num3 = int(input('Digite um numero qualquer = '))

lista = num1, num2, num3

print (f'O maior número é o {max(lista)} ')
print (f'O menor número é o {min(lista)} ')