#Desafio 19: Um professor que sortear um dos seus quatros
#alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o nome do escolhido

import random

aluno_1 = input('Primeiro aluno: ')
aluno_2 = input('Segundo aluno: ')
aluno_3 = input('Terceiro aluno: ')
aluno_4 = input('Quarto aluno: ')
lista = [aluno_1, aluno_2, aluno_3, aluno_4]
lista = random.choice(lista)

print (f'O aluno escolhido foi {lista}')