
"""
EXERCÍCIO 2
Faça um programa que leia o nome de uma pessoa
e mostre uma mensagem de boas vindas.
"""

#esse é um jeito de fazer
nome = input('Digite aqui seu nome: ')
print ('É um prazer te conhecer,', nome)

#esse é outro jeito de fazer
nome = input ('Digite seu nome: ')
print ('É um prazer te conhecer, {}!'.format(nome))

#e essa é a forma atualizada dele
nome = input('Digite seu nome: ')
print (f"É um prazer te conhecer, {nome}!")