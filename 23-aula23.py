# Autor: Sâmia
# Este algoritmo solicita ao usuário um número
# e exibe a tabuada desse número de 1 a 10.

numero = int(input("Digite um número para ver a tabuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")