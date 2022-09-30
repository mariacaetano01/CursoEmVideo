#Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
for p in range(0,5):
    peso = float(input('Seu peso: '))

    if peso > maior: 
        maior = peso
    if peso < menor:
        menor = peso

print (f'menor = {menor}')
print (f'maior = {maior}')