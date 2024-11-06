# Cria uma lista com as notas
notas = [8, 3, 5, 10]

# Imprime cada elemento da lista
for i in range(len(notas)):
    print(f"Nota {i+1}:", notas[i])

# Modifica o primeiro elemento da lista
notas[0] = 9
print("Novo valor da primeira nota:", notas[0])

# Calcula o maior, o menor e a soma das notas
maior = max(notas)
menor = min(notas)
soma = sum(notas)

# Imprime os resultados
print("Lista de notas:", notas)
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Soma de todas as notas:", soma)
