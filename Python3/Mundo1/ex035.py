'''
Desenvolva um programa que leia o comprimento
de três retas e diga ao usuário se elas podem
ou não formar um triângulo.
'''

#condição básica para um triângulo existir
# a < b + c
# b < c + a
# c < a + b

print ("Vamos ver se alguns valores formam triângulo?")
a = int(input('Lado 1 = '))
b = int(input('Lado 2 = '))
c = int(input('Lado 3 = '))

if a+b>c and c+b>a and a+c>b:
    print ('Isso é um triângulo!')
else:
    print ('Isso não é um triângulo!') 