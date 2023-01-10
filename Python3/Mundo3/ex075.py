# Desenvolva um programa que leia quatro valores pelo 
# teclado e guarde-os em uma tupla. No final, mostre:
    # A) Quantas vezes apareceu o valor 9.
    # B) Em que posição foi digitado o primeiro valor 3.
    # C) Quais foram os números pares.

nums = (int(input("Digite um valor: ")),
        int(input("Digite um valor: ")),
        int(input("Digite um valor: ")),
        int(input("Digite um valor: ")),
)

print (f"Você digitou os valors {nums}")
print (f"O valor 9 apareceu {nums.count(9)} vezes")
print (f"O valor 3 apareceu na {nums.index(3)+1}ª posição") if 3 in nums else print(f"O 3 não aparece")
print (f"Números pares digitados = {[n for n in nums if n % 2 == 0]}")