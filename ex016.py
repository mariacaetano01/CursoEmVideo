#Desaifio 16: Crie um programa que leia um número real
#qualquer pelo teclado e mostre na tela a sua porção int
#exemplo: o float 6.127 tem seu int 6

from math import trunc

print ('Me dê um número float e vou quebrá-lo em um int')
num = float(input('Digite aqui o número: '))
novo = trunc (num)
print (f'A parte inteira de {num} é {novo}')