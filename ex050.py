#Desenvolva um programa que leia seis números
#inteiros e mostre a soma apenas daqueles que
#forem pares. Se o valor digitado for ímpar,
#desconsidere-o.

sum = 0
for contador in range (1,7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        sum += num
print (f'soma = {sum}')