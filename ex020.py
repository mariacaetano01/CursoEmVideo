#Desafio 20: o mesmo professor do desaio anterior
#quer sortear a ordem de apresentação de trabalhos
#dos alunos. Faça um programa que leia o nome dos
#quatro alunos e mostre a ordem sorteadas.

import random

aluno_1 = input('Primeiro aluno: ')
aluno_2 = input('Segundo aluno: ')
aluno_3 = input('Terceiro aluno: ')
aluno_4 = input('Quarto aluno: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
#variavel = ramdom.shuffe() resulta em NONE
random.shuffle(lista)
print (f'A ordem é = {lista}')