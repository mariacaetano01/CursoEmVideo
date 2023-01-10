#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade
#e quantas já são maiores.

maior = 0
menor = 0

for pessoa in range(0,7):
    data = str(input('\033[37mData de nascimento = '))
    dia,mes,ano = data.split('/')
    ano = int(ano)
    if abs(2022-ano) < 18:
        print ('\033[31mÉ de menor')
        menor =+ 1
    elif abs(2022-ano) >= 18:
        print ('\033[32mÉ de maior!')
        maior += 1
    
print (f'\033[37mTem {maior} pessoas de maior \ne {menor} pessoas de menor')
    


