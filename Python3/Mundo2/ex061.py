#Refaça o DESAFIO 51, lendo o primeiro termo
#e a razão de uma PA, mostrando os 10 primeiros
#termos da progressão usando a estrutura while.

    #Desenvolva um programa que leia o primeiro
    #termo e a razão de uma PA. No final, mostre
    #os 10 primeiros termos dessa progressão.

        #primeiro = int(input('Primeiro termo da PA: '))
        #razao = int(input('Razão da PA: '))
        #decimo = (primeiro + (10-1)) * razao

        #for contador in range (primeiro, decimo, razao):
            #print(contador, end = ' ♥ ') 


print ("Vamos fazer uma PA")
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))
contador = 1
print (f'1º termo: {termo}')
while contador < 10:
    contador += 1
    termo = termo + razao
    print (f"{contador}º termo: {termo}")

