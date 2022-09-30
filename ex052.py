# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.

num = int(input('\n\033[m Digite aqui: '))
tot = 0

for contador in range(1, num+1):
    if num % contador == 0:
        print(f'\033[31m{contador}', end=' ')
        tot += 1
    else:
        print(f'\033[37m{contador}', end=' ')

if tot > 2:
    print(f'\n\033[31mO número {num} não é primo')
elif tot <= 2:
    print(f'\n\033[32mO número {num} é primo')
