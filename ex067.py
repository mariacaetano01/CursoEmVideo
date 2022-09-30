#Faça um programa que mostre a tabuada de vários
#números, um de cada vez, para cada valor digitado
#pelo usuário. O programa será interrompido quando
#o número solicitado for negativo.

print ("Posso te ajuda com a tabuada?")

continua = 'S'
while continua in "Ss":
    num = int(input("Digite um valor: "))
    if num < 0:
        print("Não podemos usar números negativos aqui :(")
        break
    num = int(num)
    print (f"{num} x 1 = {num*1}")
    print (f"{num} x 2 = {num*2}")
    print (f"{num} x 3 = {num*3}")
    print (f"{num} x 4 = {num*4}")
    print (f"{num} x 5 = {num*5}")
    print (f"{num} x 6 = {num*6}")
    print (f"{num} x 7 = {num*7}")
    print (f"{num} x 8 = {num*8}")
    print (f"{num} x 9 = {num*9}")
    print (f"{num} x 10 = {num*10}")

    continua = str(input("Quer saber outra? [S/N]: ")).strip().upper()[0]
    while continua not in "SsNn":
        print ("Resposta inválida.")
        continua = str(input("Quer saber outra? [S/N]: ")).strip().upper()[0]
    else:
        if continua in "Nn":
            break

print ("Obrigado por usar este programa ♥")
