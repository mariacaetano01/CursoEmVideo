'''
Faça um programa que leia um número de 0 a 9999 
e mostre na tela cada um dos dígitos separados.
'''

print ("Digite um número inteiro entre 0 e 9999:")
num = int(input(''))

#pega o resto da divisão e divide por
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print (f'O milhar do seu número é {m}')
print (f'A centena do seu número é {c}')
print (f'A dezena do seu número é {d}')
print (f'A unidade do seu número é {u}')