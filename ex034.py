'''
Escreva um programa que pergunte o salário de
um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um
aumento de 10%. Para os inferiores ou iguais, o
aumento é de 15%.
'''

print ('Haverá um aumento de salário!')
salario = float(input("Me diga o seu salário: "))

salario_10 = (salario*0.10) + salario
salario_15 = (salario*0.15) + salario 

if salario <= 1250.00:
    print (f'Seu novo salário é de {salario_10}')
else:
    print (f'Seu novo salário é de {salario_15}')