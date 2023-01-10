# Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando
# os espaços. Exemplos de palíndromos:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROT
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA.

print("VERIFICADOR DE PALÍNDROMO")
texto = str(input('\033[37mDigite aqui: '))
texto = texto.lower()
texto = texto.replace(' ', '')

# não precisa do for (eu já sabia)
for contador in texto[::-1]:
    print(contador, end=' ')

if texto == texto[::-1]:
    print('\033[32mÉ UM PALÍNDROMO')
elif texto != texto[::-1]:
    print('\033[31mNÃO É UM PALÍNDROMO\033[m')
