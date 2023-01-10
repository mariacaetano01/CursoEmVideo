# Crie um programa que leia o nome e o preço de
# vários produtos. O programa deverá perguntar
# se o usuário vai continuar ou não. No final,
# mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print("Bem-vindo ao caixa de auto-atendimento")
print("Estou aqui para ajudar!")
print(' ')
contador = soma = caro = menor = 0

while True:
    print("Por favor, digite o nome do produto.")
    produto = str(input("Digite aqui: "))
    print("Por favor, digite o valor do produto.")
    valor = float(input("Digite aqui: R$"))
    contador += 1
    soma += valor
    
    if contador == 1:
        menor = valor
    if valor < menor:
        menor = valor
    if menor == valor:
        barato = produto

    if valor > 1000:
        caro += 1

    print("Deseja inserior outro produto?")
    continua = str(input("Digite aqui: [S/N}")).strip().upper()[0]
    while continua not in "SN":
        print("Resposta inválida.")
        continua = str(input("Digite aqui: [S/N}")).strip().upper()[0]
    if continua == "N":
        break

print(f"o valor total da sua compra é de R${soma}")
print(f"Entre seus itens, existem {caro} produtos mais caros que R$1000,00")
print(f"O produto mais barato é o {barato} R${menor}")
