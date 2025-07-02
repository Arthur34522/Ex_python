nota = []
nota += [int(input("Digite a primeira nota: "))]
nota += [int(input("Digite a segunda nota: "))]
nota += [int(input("Digite a terceira nota: "))]
nota += [int(input("Digite a quarta nota: "))]
print("As notas são: ", nota)
media = (nota[0] + nota[1] + nota[2] + nota[3]) / 4
print("A média é: ", media)