# Desenvolva um programa que leia o nome, idade
# e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo
# qual é o nome do homem mais velho
# quantas mulheres têm menos de 20 anos.

maior = 0
mulher_menos_vinte = 0
media = 0
print('Digite o nome, idade e sexo do seu grupo')
print ('Para idade, somente números')
print ('Para feminino = f e masculino = m')
print(' ')

for n, i in enumerate(range(0, 4)):
    nome = str(input("Nome: "))
    idade = int(input('Idade: '))
    sexo = str(input("Sexo: "))
    print (' ')

    # media de idades
    media += idade/4

    # definir a maior idade
    if i == 1 and sexo == 'm':
        maior = idade
    elif idade > maior and sexo == 'm':
        maior = idade

    # nome do homem mais velho:
    if idade == maior and sexo == 'm':
        mais_velho = nome

    # quantidade de mulheres com menos de 20 anos:
    if idade < 20 and sexo == 'f':
        mulher_menos_vinte += 1

print(' ')
print(f'A media de idades desse grupo é: {media} anos')
print(f'O homem mais velho é o {mais_velho}, ele tem {maior} anos')
print(f'Nesse grupo tem {mulher_menos_vinte} mulheres com menos de 20 anos')
