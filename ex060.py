#Faça um programa que leia um número qualquer
#e mostre o seu fatorial. Exemplo:
    #5! = 5 x 4 x 3 x 2 x 1 = 120
#não usar "from math import factorial"

print ("Resolvendo fatoriais!!!")
num = int(input("Fatorial de: "))
contador = num
fator = 1

while contador > 0:
    print (contador,end='')
    #é possível colocar if dentro de print :)
    print (' x ' if contador>1 else ' = ', end='')
    fator *= contador
    contador -= 1 
print (fator)
    

    