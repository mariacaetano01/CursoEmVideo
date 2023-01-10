# A Confederação Nacional de Natação precisa de
#um programa que leia o ano de nascimento de um
#atleta e mostre sua categoria, de acordo com a
#idade:
    # Até 9 anos: MIRIM
    # Até 14 anos: INFANTIL
    # Até 19 anos: JÚNIOR
    # Até 25 anos: SÊNIOR
    # Acima de 25 anos: MASTER

from datetime import date

print ("PROGRAMA CLASSIFICADOR DE ATLETAS!")
print ("Digite a data de nacimento no formato dd/mm/aaa")
data = str(input("Quando seu aluno nasceu? "))

#data atual
today = date.today()
today = str(today)
ano_hoje, mes_hoje, dia_hoje = today.split('-')
ano_hoje = int(ano_hoje)

#data nascimento
dia, mes, ano = data.split('/')
ano = int(ano)

idade = ano_hoje - ano

if idade <= 9:
    print (f"Seu aluno tem {idade} anos")
    print ('categoria MIRIM')
elif 9 < idade <= 14:
    print (f"Seu aluno tem {idade} anos")
    print ('categoria INFANTIL')
elif 14 < idade <= 19:
    print (f"Seu aluno tem {idade} anos")
    print ('categoria JÚNIOR')
elif 19 < idade < 25:
    print (f"Seu aluno tem {idade} anos")
    print ('categoria SÊNIOR')
else:
    print (f"Seu aluno tem {idade} anos")
    print ('categoria MASTER')
