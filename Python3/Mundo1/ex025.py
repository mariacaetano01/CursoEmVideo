'''
 Crie um programa que leia o nome de uma
 pessoa e diga se ela tem “SILVA” no nome
'''

nome = input('Qual seu nome? ')
nome = nome.lower()
print ('silva' in nome)
#função in sozinha também devolve valor bool
