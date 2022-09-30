'''
Faça um programa que leia algo pelo teclado e mostre
na tela o seu tipo primitivo e todas as informações
possíveis sobre ele.
'''

#Excercícios para definir strings
print ('Tudo sobre uma variável!')
v = input ('Digite uma variável: ')
print ('O tipo primitivo dessa variável é', type(v))
#Verificar se tem apenas espaços
print ('Só tem espaços?', v.isspace())
#Verificar se é apenas numérico
print ('É numérico?', v.isnumeric())
#Verificar se é um texto
print ('É um texto?', v.isalpha())
#Verificar se é alfanumérico
print ('É alfanumérico?!', v.isalnum())
#Verificar se está todo em caixa alta
print ('Está em letras maiúsculas?,', v.isupper())
#Verificar se está todos em caixa baixa
print ('Está em letras minúsculas?', v.islower()) 
#Está com a primeira letra maiúscula e as demais minúsculas?
print ('É um título?', v.istitle())
