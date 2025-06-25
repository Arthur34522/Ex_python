num1=float(input(f"Digite o primeiro número: "))
num2=float(input(f"Digite o segundo número: "))
calculo=input(f"Digite a operação desejada (+, -, *, /): ")
if calculo == "+":
    resultado = num1 + num2
elif calculo == "-":
    resultado = num1 - num2
elif calculo == "*":
    resultado = num1 * num2
elif calculo == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
print(f"O resultado da operação {num1} {calculo} {num2} é: {resultado}")