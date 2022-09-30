#Faça um programa que leia o ano de nascimento de
#um jovem e informe, de acordo com a sua idade, se 
#ele ainda vai se alistar ao serviço militar, se é 
#a hora exata de se alistar ou se já passou do tempo
#do alistamento. Seu programa também deverá mostrar
#o tempo que falta ou que passou do prazo.

from datetime import date

print ('PROGRMA PARA ALISTAMENTO MILITAR')
print ('Esse programa vai te dizer quando se alistar!')

nascimento = str(input("Digite sua data de nascimento (entre barras): "))


dia, mes, ano = nascimento.split("/")
dia = int(dia) 
mes = int(mes)
ano = int(ano)

today = date.today()
today = str(today)
ano_hoje, mes_hoje, dia_hoje = today.split('-')
dia_hoje = int(dia_hoje)
mes_hoje = int(mes_hoje)
ano_hoje = int(ano_hoje)

ano_certo = ano + 18
idade = ano_hoje - ano


if idade < 18:
    if dia_hoje < dia and mes_hoje < mes:
        print ('Você ainda não pode se alistar')
        print (f'Ainda faltam {(-1)*(dia_hoje-dia)} dias, {(mes_hoje-mes)} meses e {(-1)*(ano_hoje-ano_certo)} anos')
    elif dia_hoje >= dia and mes_hoje > mes:
        print ('Você ainda não pode se alistar')
        print (f'Ainda faltam {(dia_hoje-dia)} dias, {(mes_hoje-mes)} meses e {(-1)*(ano_hoje-ano_certo)} anos')
    elif dia_hoje >= dia and mes_hoje < mes:
        print ('Você ainda não pode se alistar')
        print (f'Ainda faltam {(dia_hoje-dia)} dias, {(-1)*(mes_hoje-mes)} meses e {(-1)*(ano_hoje-ano_certo)} anos')
    elif dia_hoje < dia and mes_hoje > mes:
        print ('Você ainda não pode se alistar')
        print (f'Ainda faltam {(-1)*(dia_hoje-dia)} dias, {(mes_hoje-mes)} meses e {(-1)*(ano_hoje-ano_certo)} anos')
elif idade == 18:
    print ("Você pode se alistar!")
elif idade > 18:
    if dia_hoje <= dia and mes_hoje < mes:
        print ("Já passou do tempo de se alistar!")
        print (f"Já se passaram {(dia-dia_hoje)} dias, {(mes-mes_hoje)} meses e {(-1)*(ano_certo-ano_hoje)} anos!")
    elif dia_hoje > dia and mes_hoje > mes:
        print ("Já passou do tempo de se alistar!")
        print (f"Já se passaram {(-1)*(dia-dia_hoje)} dias, {(-1)*(mes-mes_hoje)} meses e {(-1)*(ano_certo-ano_hoje)} anos!")
    elif dia_hoje > dia and mes_hoje < mes:
        print ("Já passou do tempo de se alistar!")
        print (f"Já se passaram {(-1)*(dia-dia_hoje)} dias, {(mes-mes_hoje)} meses e {(-1)*(ano_certo-ano_hoje)} anos!")
    elif dia_hoje <= dia and mes_hoje > mes:
        print ("Já passou do tempo de se alistar!")
        print (f"Já se passaram {(dia-dia_hoje)} dias, {(-1)*(mes-mes_hoje)} meses e {(-1)*(ano_certo-ano_hoje)} anos!")

print ("OBRIGADO POR USAR ESTE PROGRAMA")
