#Crie um programa que leia duas notas de um aluno
#e calcule sua média, mostrando uma mensagem no
#final, de acordo com a média atingida:
    # Média abaixo de 5.0: REPROVADO
    # Média entre 5.0 e 6.9: RECUPERAÇÃO
    # Média 7.0 ou superior: APROVADO


print ("PROGRAMA VERIFICADOR DE NOTAS")
print ("Digite a seguir as notas do aluno:")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))

media = round(((n1+n2)/2),2)

if media < 5.0:
    print (f'A média do aluno é {media}')
    print ("ALUNO REPROVADO")
elif 5.0 <= media < 7.0:
    print (f'A média do aluno é {media}')
    print ("ALUNO EM RECUPERAÇÃO")
else:
    print (f'A média do aluno é {media}')
    print ("ALUNO APROVADO")

print ('  ')
print ('OBRIGADO POR USAR ESTE PROGRAMA!')