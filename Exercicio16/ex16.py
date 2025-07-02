def contar_digitos(numero):
  
    return len(str(abs(numero)))
    
def main(): 
    try:
        numero = int(input("Digite um número: "))
        quantidade_digitos = contar_digitos(numero)
        print(f"O número {numero} possui {quantidade_digitos} dígitos.")
    except ValueError:
        print("Por favor, digite um número válido.")
if __name__ == "__main__":
    main()
