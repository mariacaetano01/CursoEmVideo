'''
Escreva um programa que pergunte a quantidade de
Km percorridos por um carro alugado e a quantidade
de dias pelos quais ele foi alugado. Calcule o preço
 a pagar, sabendo que o carro custa R$60 por dia e 
 R$0,15 por Km rodado.
'''

print ('Preço do Aluguel')
dia = 60
km = 0.15
print ('O dia custa R$60,00 e o km rodado R$0,15')
dia_rodado = float(input('Por quantos dias ficou com o carro? '))
km_rodado = float(input('E quantos km você rodou? '))
print(f'O total a pagar é de R${(dia*dia_rodado)+(km*km_rodado)}')