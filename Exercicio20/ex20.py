letras= ["a","b","c","d","e","f",]
var = input("informe uma letra ser verificada:")
if var.lower() in letras:
    print(f"A letra '{var.lower()}' está na lista.")
else:
    print(f"A letra '{var.lower()}' não está na lista.")