lista= []
lista.append(int(input("Digite um número (ou 0 para sair): ")))
while True:
    
        num = int(input("Digite um número (ou 0 para sair): "))
        if num == 0:
            break
        lista.append(num)
lista.reverse()
print("Lista invertida:", lista)