#Crie um programa que leia a idade e o sexo
#de várias pessoas. A cada pessoa cadastrada,
#o programa deverá perguntar se o usuário quer
# ou não continuar. No final, mostre:
    # A) quantas pessoas tem mais de 18 anos.
    # B) quantos homens foram cadastrados.
    # C) quantas mulheres tem menos de 20 anos.

cont_18 = cont_h = cont_m = 0
print('Digite idade e sexo do seu grupo')

while True:

    idade = int(input('Idade(somente números): '))
    sexo = str(input("Sexo[F/M]: ")).strip().upper()[0]
    if sexo not in "FfMm":
        print ("Valor inválido. Tente novamente.")
        continue

    if idade > 18:
        cont_18 += 1
    if sexo in "Mm":
        cont_h += 1
    if sexo in "Ff" and idade <20:
        cont_m += 1

    continua = str(input("Deseja fazer outro cadastro? [s/n]: ")).strip().upper() [0]
    if continua not in "SsNn":
        while continua not in "SsNn":
            print ("Valor inválido. Tente novamente.")
            continua = str(input("Deseja fazer outro cadastro? [s/n]: ")).strip().upper() [0]
    elif continua in 'Nn':
        break

print(f'Seu grupo tem {cont_18} maiores de 18 anos;')
print(f'Seu grupo tem {cont_h} homens cadastrados;')
print(f'Seu grupo tem {cont_m} mulheres com menos de 20 anos')
print (' ')
print("Obrigado por usar este programa")
print(" ")