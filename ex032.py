'''
Faça um programa que leia um ano qualquer
e mostre se ele é bissexto.
'''

from time import sleep


print ('Vamos descobrir se um ano é bissexto?')
ano = int(input('Que ano você quer saber? '))

print(' ')
print ('Para um ano ser bissexto ele deve ser divisível por 4')
print ('Caso ele seja centenário, deve ser divisível por 400')

sleep(2)
print(' ')

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print ('Esse é um ano bissexto')
else:
    print ('Esse não é um ano bissexto')