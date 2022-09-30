'''
Desenvolva um programa que pergunte a distância
de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e
R$0,45 parta viagens mais longas.
'''

print ('Vamos descobrir o preço da passagem?')
print ('Primeiro me diga quantos km você vai viajar?')
distancia = float(input('Digite aqui: '))

km_200 = distancia * 0.5
km_201 = distancia * 0.45

if distancia <= 200:
    print (f'O valor da passagem é de R${km_200}')
else:
    print(f'O valor da passagem é de R${km_201}')