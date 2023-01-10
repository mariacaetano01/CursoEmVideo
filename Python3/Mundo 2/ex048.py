#Faça um programa que calcule a soma entre
#todos os números que são múltiplos de três,
#que são ímparese que se encontram no intervalo
#de 1 até 500.

soma = 0
cont = 0
for contador in range (1,501,2):
    if contador %3 == 0:
        print (contador)
        cont = cont + 1
        soma = soma + contador
print (f'existem {cont} multiplios de 3 entre 1 e 500')
print (f'a soma de todos esss valores é = {soma}')