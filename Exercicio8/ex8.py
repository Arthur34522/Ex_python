nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f"A média é {media:.1f}, você foi aprovado.")
elif media >= 4:
    print(f"A média é {media:.1f}, você está de recuperação.")
else:
    print(f"A média é {media:.1f}, você foi reprovado.")