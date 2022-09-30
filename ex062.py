#Melhore o DESAFIO 61, perguntando para
#o usuário se ele quer mostrar mais alguns
#termos. O programa encerrará quando ele
#disser que quer mostrar 0 termos.

        #print ("Vamos fazer uma PA")
        # termo = int(input("Digite o primeiro termo: "))
        # razao = int(input("Digite a razão da PA: "))
        # contador = 1
        # print (f'1º termo: {termo}')
        # while contador < 10:
            #contador += 1
            #termo = termo + razao
            #print (f"{contador}º termo: {termo}")

print ("Vamos fazer uma PA")
termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))
contador = 1
print (f'1º termo: {termo}')
while contador < 10:
    contador += 1
    termo = termo + razao
    print (f"{contador}º termo: {termo}")

continua = str(input("Você quer continuar com a PA? [S/N]: ")).strip().upper() [0]
while continua not in "SN":
    print('Resposta Inválida, digite novamente.')
    continua = str(input("Você quer continuar com a PA? [S/N]: ")).strip().upper() [0]
    if continua == 'N':
        print ("Acabamos por aqui!")
        break
    elif continua == 'S':
        print ("Até que temo você precisa?")
        novotermo = int(input("Digite novo termo: "))
        while contador < novotermo:
            contador += 1
            termo = termo + razao
            print (f"{contador}º termo: {termo}")

print (' ')
print ('Obrigado por usar este programa ♥')