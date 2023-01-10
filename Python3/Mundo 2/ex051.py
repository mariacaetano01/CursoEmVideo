#Desenvolva um programa que leia o primeiro
#termo e a razão de uma PA. No final, mostre
#os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))
decimo = (primeiro + (10-1)) * razao

for contador in range (primeiro, decimo, razao):
    print(contador, end = ' ♥ ')