# Crie um programa que leia vários números
# inteiros pelo teclado. No final da execução,
# mostre a média entre todos os valores e qual
# foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não
# continuar a digitar valores.


contador = maior = menor = soma = 0
continua = "S"

while continua == "S":
    num = input("Digite um valor: ")
    if not num.isnumeric:
        print("Resposta inválida")
        num = input("Digite um valor: ")
    
    num = int(num)
    soma += num
    contador +=1
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continua = str(input("Quer digitar outro número? [S/N]: ")).strip().upper()[0]
    while continua not in 'SsNn':
        print("Resposta inválida.")
        continua = str(input("Quer digitar outro número? [S/N]: ")).strip().upper()[0]
    else:
        if continua == 'N':
            print("Então acabamos por aqui")
            print(' ')
            print(f"você digitou {contador} números")
            print(f"A media de seus números é = {round((soma/contador),2)}")
            print(f"O maior número que você digitou foi {maior}")
            print(f"O menor número que você digitou foi {menor}")
            break
        else:
            continue
