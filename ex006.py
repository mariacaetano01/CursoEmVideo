#Desafio 06
'''
Crie um algoritmo que leia um número e
mostrei seu dobro, triplo e sua raiz
quadrada.
'''
print ('Qual o dobro, triplo e raiz?')
print ('Vamos Descobrir!')
valor = float(input("Digite um número: "))
dobro = valor + valor
triplo = dobro + valor
raiz = valor ** (1/2)
print (f'O dobro de {valor} é {dobro}')
print (f'O triplo de {valor} é {triplo}')
print (f'A raiz de {valor} é {raiz}')

#Desafio 06 (feito com import.math)
'''
Crie um algoritmo que leia um número e
mostrei seu dobro, triplo e sua raiz
quadrada.
'''
print ('Qual o dobro, triplo e raiz?')
print ('Vamos Descobrir!')
from math import sqrt
valor = float(input("Digite um número: "))
dobro = valor + valor
triplo = dobro + valor
raiz = sqrt(valor)
print (f'O dobro de {valor} é {dobro}')
print (f'O triplo de {valor} é {triplo}')
print (f'A raiz de {valor} é {raiz}')