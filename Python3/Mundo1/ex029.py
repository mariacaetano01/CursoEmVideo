'''
 Escreva um programa que leia a velocidade de
 um carro. Se ele ultrapassar 80Km/h, mostre
 uma mensagem dizendo que ele foi multado.
 A multa vai custar R$7,00 por cada Km acima
 do limite.
'''

from time import sleep


print ('Você sabia que a velocidade aqui é 80km/h?')
print ('A quantos km/h você estava quando passou pelo rada?')
radar = float(input(''))
multa = (radar-80) * 7

print ('CALCULANDO...')
sleep (2)

if radar <= 80:
    print ('Ufa! Então não levou multa!')
else:
    print ('Você ultrapassou o limite de velocidade!')
    print (f'A sua multa é de {multa} reais')