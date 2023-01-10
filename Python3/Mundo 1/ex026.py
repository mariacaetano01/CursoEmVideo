'''
Faça um programa que leia uma frase pelo teclado
e mostre quantas vezes aparece a letra “A”, em
que posição ela aparece a primeira vez e em que
posição ela aparece a última vez.
'''

frase = input('Diga-me uma frase: ')
frase = frase.replace('á','a')
frase = frase.replace('Á','a')
frase = frase.replace('â','a')
frase = frase.replace('Â','a')
frase = frase.replace('ã','a')
frase = frase.replace('Ã','a')

frase = frase.strip()
frase = frase.lower()

conta = frase.count ('a')
pos1 = frase.find('a')
pos2 = frase.rfind('a')

if conta >= 1:
    print (f'Na sua frase, a letra "a" aparece {conta} vezes')
    print (f'A sua primeira aparição fica na posição {pos1+1}')
    print (f'A sua última aparição fica na posição {pos2+1}')
else:
    print ('Não tem a letra "A" na sua frase')