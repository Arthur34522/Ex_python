def main():
    soma = 0
    while True:
        try:
            numero = int(input("Digite um número inteiro (0 para sair): "))
            if numero == 0:
                break
            soma += numero
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
    print(f"A soma de todos os números digitados é: {soma}")
if __name__ == "__main__":
    main()
