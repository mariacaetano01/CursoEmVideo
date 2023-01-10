'''
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço com 5(%) de desconto
'''
print ('Hoje tem promoção!')
valor = float(input('Qual o valor do seu produto? R$'))
#desconto = número em porcentagem
desconto = 5
print (f'Pois agora esse produto é R${valor - (valor * (desconto/100))}')