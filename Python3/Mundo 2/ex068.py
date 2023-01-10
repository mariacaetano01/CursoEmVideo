# Faça um programa que jogue par ou ímpar
# com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de
# vitórias consecutivas que ele conquistou no
# final do jogo.

import random
from time import sleep
from timeit import repeat
print("Vamos jogar ímpar ou par?")
cont = 0

while True:
    print(' ')
    print("[ 1 ] IMPAR")
    print("[ 2 ] PAR")
    jogada = str(input("ímpar ou par? "))

    if jogada not in "12":
        print("Valor inválido, vamos tentar de novo")
        continue

    jogada_us = int(input("Qual sua jogada? "))
    jogada_pc = random.randint(0, 10)
    soma = jogada_pc + jogada_us
    print(f'Computador: {jogada_pc}')

    print("Carregando resposta...")
    sleep(2)
    if jogada == '1':
        if soma % 2 != 0:
            print(f'Soma = {soma}. Você venceu!')
            cont += 1
        else:
            print(f"Soma = {soma}")
            break
    elif jogada == '2':
        if soma % 2 == 0:
            print(f'Soma = {soma}. Você venceu!')
            cont += 1
        else:
            print(f"Soma = {soma}")
            break
    print("Vamos jogar de novo?")
    sleep(2)

print("Game over, eu ganhei!")
print(f"Durante o jogo, você venceu {cont} vezes!")