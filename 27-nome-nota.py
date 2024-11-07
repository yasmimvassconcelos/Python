# Dicionário para armazenar os alunos
alunos = {}

# Pergunte quantos alunos existem
qtd_alunos = int(input("Quantos alunos? "))

# Leia os nomes e notas
for i in range(qtd_alunos):
    nome = input(f"Nome do aluno {i+1}: ")
    nota = float(input(f"Nota do aluno {i+1}: "))
    
    # Adicione ao dicionário
    alunos[nome] = nota

# Exiba os resultados
print("\nResultados:")
for nome, nota in alunos.items():
    print(f"{nome}: {nota}")