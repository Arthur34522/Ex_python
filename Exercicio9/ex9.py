pessoa= input(" Digite c para casado, d para divorciado, s para solteiro, v para viúvo: ")
if pessoa == "c":
    print("Você é casado(a).")
elif pessoa == "d":
    print("Você é divorciado(a).")
elif pessoa == "s":
    print("Você é solteiro(a).")
elif pessoa == "v":
    print("Você é viúvo(a).")
else:
    print("Outro estado civil.")