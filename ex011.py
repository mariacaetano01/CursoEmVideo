'''
Faça um programa que leia a altura e a largura
de uma parede em metros, calcule a sua àrea e 
a quantidade de tinta necessária para pinta-la,
sabendo que cada litro de tinta cobre uma àrea
de 2m²
'''
print ('Quantas latas precisa para pintar ujma parde?')
l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
area = l * a
cob_por_litro = 2
print (f'A area da parede é de {area} metros quadrados')
print (f'Você vai precisar de {(area/cob_por_litro)} litros de tinta')