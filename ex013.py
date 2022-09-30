'''
Faça um algoritmo que leia o salário de um 
funcionário e mostre seu novo salário, com
15(%) de aumento.
'''

s = float(input('Digite aqui seu salário atual: R$'))
#aumento = número em porcentagem
aumento = 15
print (f'Seu salário vai aumentar em 15%')
print (f'Seu novo salário é de {s + (s * (15/100))}')