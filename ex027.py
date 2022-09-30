'''
Faça um programa que leia o nome completo de
uma pessoa, mostrando em seguida o primeiro e
o último nome separadamente.
'''
nome = input('Digite seu nome completo aqui: ')
n = nome.split()

print ('Muito prazer ♥')
print (f'Seu primeiro nome é: {n[0]}')
print (f'Seu último nome é: {n[-1]}')