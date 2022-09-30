#Escreva um programa para aprovar o empréstimo
#bancário para a compra de uma casa. Pergunte
#o valor da casa, o salário do comprador e em 
#quantos anos ele vai pagar. A prestação mensal 
#não pode exceder 30% do salário ou então o
#empréstimo será negado.

print ("Vamos ver se você pode pegar um empréstimo ?")

casa = float(input("Qual o valor da casa que você quer? "))
salario = float(input("Qual o seu salário atual? "))
anos = float(input("Em quantos anos você pretende pagar? "))

parcela = round(((casa/anos)/12),2)
terco_salario = (salario*0.3)

if parcela <= terco_salario:
    print (f"Sua parcela é de R${parcela}")
    print ("Seu empréstimo será APROVADO")
elif parcela > terco_salario:
    print (f"Sua parcela é de R${parcela}")
    print ("Seu empréstimo será NEGADO")
    print ("Procure uma casa mais barata ou pague em mais vezes")
else:
    print ("ERRO")