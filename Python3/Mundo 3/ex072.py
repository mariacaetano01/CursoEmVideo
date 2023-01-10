# Crie um programa que tenha uma dupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte. Seu programa
# deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
# por extenso.

números = (
    'zero',
    'um',
    'dois',
    'três',
    'quatro',
    'cinco',
    'seis',
    'sete',
    'oito',
    'nove',
    'dez',
    'onze',
    'doze',
    'treze',
    'quatorze',
    'quinze',
    'deszesseis',
    'dezessete',
    'dezoito',
    'dezenove',
    'vinte'
)

print("Como se escreve meu número?")

while True:
    num = int(input('Digite um número de 0 a 20: '))

    if 0 <= num <= 20:
        print(f'Você digitou o número {números[num]}')
        game = str(input("Quer jogar de novo? "))
        game.lower()
        if game.lower() in 'sim':
            continue
        if game.lower() in "naonão":
            print("Obrigado por usar este programa!")
            break
        else:
            while game.lower() not in "simnaonão":
                gg = str(input("Essa resposta não é válida. Quer jogar de novo? "))

    else:
        print("Você digitou um número fora do intervalo!\n")
