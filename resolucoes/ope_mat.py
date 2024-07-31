# Vamos solicitar como entrada dois números e depois vamos
# realizar uma operação

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
operacao = input("Digite qual a operação a realizar: (+, -, /, *): ")

if (operacao == "+"):
    resultado = num1 + num2
elif (operacao == "-"):
    resultado = num1 - num2 
elif (operacao == "/" ):
    resultado = num1 / num2 
elif (operacao == "*"):
    resultado = num1 * num2

print(resultado)