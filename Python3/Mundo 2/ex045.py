#GAME PEDRA PAPEL TESOURA
#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

print ("VAMOS JOGAR JOKENPÔ - PEDRA, PAPEL, TESOURA!")
print ("Digite sua jogada (prometo que não vou olhar)")
print (" ")
sleep (2)

print ("[ 0 ] PEDRA")
print ("[ 1 ] PAPEL")
print ("[ 2 ] TESOURA")
jogada = int(input("Digite sua jogada: "))
print(" ")
if jogada == 0:
    print ('Você escolheu PEDRA')
elif jogada == 1:
    print ('Você escolheu PAPEL')
elif jogada == 2:
    print ('Você escolheu TESOURA')

pc = randint(0,2)
if pc == 0:
    print ('Eu escolhi PEDRA')
elif pc == 1:
    print ('Eu escolhi PAPEL')
elif pc == 2:
    print ('Eu escolhi TESOURA')

if jogada == pc:
    print ("EMPATAMOS!")
elif (jogada == 0 and pc == 1) or (jogada == 1 and pc == 2) or (jogada == 2 and pc == 0):
    print ("VOCÊ PERDEU!")
elif (jogada == 0 and pc == 2) or (jogada == 1 and pc == 0) or (jogada == 2 and pc == 1):
    print ("VOCÊ GANHOU")
else:
    print ("Algo deu errado!")