#Escreva um programa que leia um
#número N inteiro qualquer e mostre
#na tela os N primeiros elementos
#de uma Sequência de Fibonacci

print ("Sequência Fiabonacci")
elem = int(input("Digite quantos elementos a sequência terá: "))

fibonacci = [0,1]
contador = 0

while contador < (elem-2):
    contador += 1
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print (fibonacci)

