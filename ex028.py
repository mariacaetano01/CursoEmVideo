'''
Escreva um programa que faça o computador “pensar” em um
número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu 
ou perdeu.
'''

import random
from time import sleep

print ('Jogo de Advinha!!!')
print ('Vou pensar em um número e você tem que advinhar!')

num_inicial = 0
num_final = 5
print (f'Vou pensar em um número entre {num_inicial} e {num_final}')
num = int(input('Em que numero eu pensei? '))

computador = random.randint (num_inicial,num_final)

print ('PROCESSANDO...')
sleep (2)
if num == computador:
    print ('Parabéns! Você acertou!')
    print (f'Eu pensei no número {computador}')
else:
    print ('Que pena, você perdeu!')
    print (f'O numero que eu pensei foi o {computador}')


