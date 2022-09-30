'''
Crie um programa em python que leia o nome
completo de uma pessoa e mostre:
    o nome com todoas as letras maiúculas;
    o nome com todas as letras minúsculas;
    quantas letras tem todo o nome;
        (sem considerar espaços)
    quantas letras tem o primeiro nome;
'''
from time import sleep

nome = input('Qual o seu nome completo? ')
print ('Analisando seu nome...')
sleep (2)

maiusculas = nome.upper()
minusculas = nome.lower()
sem_espaço = nome.replace(' ','')
comprimento = len(sem_espaço)
primeiro, segundo, terceiro = nome.split(' ')
primeiro_comp = len(primeiro)

print ('Seu nome em maiúsculas fica assim:')
print (maiusculas)
print (f'Seu nome em minúsculas fica assim:')
print (minusculas)
print (f'Sabia que seu nome tem {comprimento} letras?')
print (f'Bom, seu primeiro nome tem {primeiro_comp} letras')