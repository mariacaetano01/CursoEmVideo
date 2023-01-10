#Faça um programa que mostre na tela uma contagem regressiva 
#para o estouro de fogos de artifício, indo de 10 até 0, com
#uma pausa de 1 segundo entre eles.

from time import sleep

print ('A CONTAGEM PARA OS FOGOS VAI COMEÇAR')
start = str(input("Digite 'start' para que os fogos comecem: "))

print ("A contagem regressiva vai começar")
for contador in range (10,0,-1):
    print (contador)
    sleep(1)
print ('*os fogos começaram*')
