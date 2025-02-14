numero1 = input("Digite um número: ")
numero2 = input("Digite outro número: ")
operacaoMat = input("Digite a operação desejada: ")

if operacaoMat == "+":
    resultado = int(numero1) + int(numero2)     
elif operacaoMat == "-":
    resultado = int(numero1) - int(numero2)
elif operacaoMat == "*":
    resultado = int(numero1) * int(numero2)
elif operacaoMat == "/":
    resultado = int(numero1) / int(numero2)
else:
    resultado = "Operação inválida"

print(resultado)


