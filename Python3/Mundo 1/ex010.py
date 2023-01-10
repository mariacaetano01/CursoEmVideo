'''
Crie um programa que leia  quanto dinheiro 
uma pessoa tem na carteira e mostre quantos
doláres ela pode comprar. Se quiser, pode 
fazer com outras moedas também
'''

print ('Quantas moedas você pode comprar?')
r = float(input('Quantos reais você tem? R$'))

dolar_hoje = 4.79
print (f'o dólar hoje está a {dolar_hoje} reais')
print (f'Você pode comprar {round((r/dolar_hoje),2)} dólares hoje')

euro_hoje = 5.13
print (f'o euro hoje está a {euro_hoje} reais')
print (f'Você pode comprar {round((r/euro_hoje),2)} euros hoje')

yen_hoje = 0.038
print (f'o yen hoje está a {yen_hoje} reais')
print (f'Você pode comprar {round((r/yen_hoje),2)} yens hoje')