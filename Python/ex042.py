#Refaça o DESAFIO 35 dos triângulos, acrescentando
#o recurso de mostrar que tipo de triângulo será
# formado:
    #EQUILÁTERO: todos os lados iguais
    # ISÓSCELES: dois lados iguais, um diferente
    # ESCALENO: todos os lados diferentes

print ("PROGRAMA VERIFICADOR DE TRIÂNGULOS")
print ("Lembrando que a unidade de medida é CENTÍMETROS")
l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if (l1+l2) < l3 or (l2+l3) < l1 or (l1+l3) < l3:
    print ("Isso não forma um triângulo!")
elif (l1+l2) < l3 or (l2+l3) > l1 or (l1+l3) > l3:
    if l1==l2 and l1!=l3 and l2!=l3:
        print ("Isso é um triângulo isóceles")
    elif l2==l3 and l1!=l3 and l2!=l1:
        print ("Isso é um triângulo isóceles")
    if l1==l3 and l1!=l2 and l2!=l3:
        print ("Isso é um triângulo isóceles")
    elif l1 != l2 and l2 != l3 and l3 != l1:
        print ('Isso é um triângulo escaleno!')
    elif l1 == l2 and l2 == l3 and l3 == l1:
        print ("Isso é um triângulo equilátero")