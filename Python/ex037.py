#Escreva um programa em Python que leia
#um número inteiro qualquer e peça para
# o usuário escolher qual será a base de
#conversão: 1 para binário, 2 para octal
#e 3 para hexadecimal.

print ("PROGRAMA PARA CODIFICAR NÚMEROS!")
print ("Primeiro, digite um número inteiro qualquer:")
inteiro = int(input("Digite aqui: "))
print ("Agora preciso saber como quer que ele \n seja decodificado!")
print ('[ 1 ] converter para BINÁRIO')
print ('[ 2 ] converter para OCTAL')
print ('[ 3 ] converter para HEXADECIMAL')
base = str(input("Digite aqui "))


#o python tem funções prontas para esse tipo de conversão
if base == '1':
    print (f'{inteiro} em binário fica {bin(inteiro)}')
elif base == '2':
    print(f'{inteiro} em octal fica {oct(inteiro)}')
elif base == '3':
    print(f'{inteiro} em hexadecimal {hex(inteiro)}')
else:
    print ("Essa opção é invalida")
    print ("O programa vai encerrar agora")

print ("Obrigado por usar este programa")
