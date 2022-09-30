'''
Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome “SANTO”.
'''
# cidade = input('Em que cidade você nasceu? ')
# cidade_grande = cidade.upper()
# cidade_final = cidade_grande.startswith('SANTO')
# print (cidade_final)

cidade = input('Em que cidade você nasceu? ')
cidade_grande = cidade.upper()
print (cidade_grande[:5] == 'SANTO')