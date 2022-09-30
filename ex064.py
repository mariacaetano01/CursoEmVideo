#Crie um programa que leia vários números
#inteiros pelo teclado. O programa só vai
#parar quando o usuário digitar o valor 999,
#que é a condição de parada. No final, mostre
#quantos números foram digitados e qual foi a
#soma entre eles (desconsiderando o flag).

num = 0
soma = 0
contador = 0

while num != 999:
    num = int(input("Digite um valor: "))
    if num == 999:
        break
    soma += num
    contador += 1
print (f"Você digitou {contador} numeros antes de 999")
print (f"A soma desses números é = {soma}")