palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")

