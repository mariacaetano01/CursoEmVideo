# Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem
# de números gerados e também indique o menor e o maior 
# valor que estão na tupla.

import random
nums = []
for _ in range(5):
    nums.append(random.randint(0,100))
print (nums)
print (f"Maior = {sorted(nums)[4]}\nMenor = {sorted(nums)[0]}")