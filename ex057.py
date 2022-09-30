# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja
# errado, peça a digitação novamente até ter um
# valor correto.

#(input).strip.upper[0]: cortar espaços, maíuscula [primeira letra]
sexo = (str(input("Digit aqui seu sexo [F/M]: "))).strip().upper()[0]
while sexo  not in "MF":
    sexo = (str(input("Dados inválidos. Digite aqui seu sexo (F/M): "))).upper()
else:
    print (f'Sexo {sexo} registrado com sucesso')