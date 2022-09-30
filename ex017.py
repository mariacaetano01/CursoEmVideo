#Desafio 17: Faça um programa que leia o comprimento 
#do cateto oposto e do cateto adjacente de um triângulo
#retângulo, calcule e mostre o comprimento da hipotenusa

print ('O quadrado da hipotenusa é igual')
print ('a soma dos quadrados dos catetos.')
cateto_1 = float(input('Digite o cateto 1: '))
cateto_2 = float(input('Digite o cateto 2: '))
hipotenusa = (((cateto_1 ** 2)+(cateto_2 ** 2)) ** (1/2))
print (f'A hipotesuna desse triangulo é = {hipotenusa}')

print('')
print('ou se for mais fácil')
print('from math import hypot')
from math import hypot
print (f'A hipotenusa ainda é {hypot(cateto_1,cateto_2)}')