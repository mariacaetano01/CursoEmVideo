'''
Escreva um programa que leia um valor em metros
e exiba convertido em centímetros e milímetros
'''

print ('Quanto vale um metro?')
m = float(input('Quantos metros quer saber? '))

# multiplica metros em 1000 vezes para milímetros
mm = m * 1000
# multiplica metros em 100 vezes para centímetros
cm = m * 100
# multiplica metros em 10 vezes para decímetros
dm = m * 10
# divide metros por 10 para decâmetros
dam = m / 10
# divide metros por 100 para hectometros
hm = m / 100
# divide metros por 1000 para quilometros
km = m * 1000

print ('Esse valor em metros é igual a:')
print (f'{mm} mm')
print (f'{cm} cm')
print (f'{dm} dm')
print (f'{dam} dam')
print (f'{hm} hm')
print (f'{km} km')
print ('Que bom que pude ajudar ♥')