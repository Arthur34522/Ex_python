
idade = input("Digite a idade do nadador: ")
idade = int(idade)
if idade >= 5 and idade <= 7:
    categoria = "Infantil 1"
elif idade >= 8 and idade <= 11:
    categoria = "Infantil 2"
elif idade >= 12 and idade <= 13:
    categoria = "Juvenil 1"
elif idade >= 14 and idade <= 17:
    categoria = "Juvenil 2"
elif idade >= 18:
    categoria = "Adulto"
print(f"A categoria do nadador é: {categoria}")
