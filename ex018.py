#Desafio 18: Faça um programa que leia um ângulo qualquer
#e mostre na tela o valor do seno, cosseno e tangente desse
#ângulo

import math

angulo = float(input("Digite um angulo: "))
sen = math.sin (math.radians(angulo))
cos = math.cos (math.radians(angulo))
tan = math.tan (math.radians(angulo))
print (f'O seno de {angulo} é {round(sen,2)}') 
print (f'O cosseno de {angulo} é {round(cos,2)}')
print (f'A tangente de {angulo} é {round(tan,2)}')