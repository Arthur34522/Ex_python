

total_alunos = 0
turma_atual = 1
alunos = 0
media = ""
quantidade_turmas = int(input("Quantas turmas? "))

while quantidade_turmas <0:
    print("Quantidade de turmas inválida. Digite um número positivo.")
    quantidade_turmas = int(input("Quantas turmas? "))
    
while turma_atual <= quantidade_turmas:
    alunos = int(input(f"Quantos alunos na turma {turma_atual}? "))
    
    while alunos < 0:
        print("Quantidade de alunos inválida. Digite um número positivo.")
        alunos = int(input(f"Quantos alunos na turma {turma_atual}? "))             

    total_alunos += alunos
    turma_atual += 1

media = total_alunos / quantidade_turmas
print(f"A média de alunos por turma é {media:.2f} alunos.")
if media < 10:
    print("A média de alunos por turma é baixa.")
elif media < 20:
    print("A média de alunos por turma é média.")
else:
    print("A média de alunos por turma é alta.")
    