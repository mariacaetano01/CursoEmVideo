# Crie uma tupla preenchida com os 20 primeiros colocados 
# da Tabela do Campeonato Brasileiro de Futebol, na ordem 
# de colocação. Depois mostre:
    # a) Os 5 primeiros times.
    # b) Os últimos 4 colocados.
    # c) Times em ordem alfabética.
    # d) Em que posição está o time da Chapecoense.

times = (
    "palmeiras",
    "internacional",
    "fluminense",
    "corinthians",
    "flamengo",
    "athletico paranaense",
    "atlético mineiro",
    "fortaleza",
    "são paulo",
    "américa MG",
    "botafogo",
    "santos",
    "goias",
    "bragantino",
    "coritiba",
    "cuiabá",
    "ceará",
    "atlético GO",
    "avaí",
    "juventude"
)

# Utilizar do conceito de slicing dentro da tupla pra alcançar um 
print ("\nTOP CINCO TIMES DO BRASILEIRAO")
for p,i in enumerate(times[:5]):
    print (f"{p+1} {i}")
    
print ("\nOS 4 ULTIMOS COLOCADOS DO BRASILEIRÃO")
for p,i in enumerate(times[16:20]):
        print (f"{p+1} {i}")

print ("\nTIMES DO BRASILEIRÃO EM ORDEM ALFABETICA")
for p,i in enumerate(sorted(times)):
    print (f"{p+1} {i}")

print ("\nPOSIÇÃO DA CHAPECOENSE NO BRASILEIRÃO")
# print (times.index("chapecoense"))
# chapecoense não está no top brasileirão no momento que esse exercício foi feito

print ("\nEM QUE POSIÇÃO SEU TIME ESTÁ NO BRASILEIRÃO?")
time = str(input("Digite seu time aqui: "))
print(times.index(time)) if time.lower() in times else print("Seu time não está na lista") 