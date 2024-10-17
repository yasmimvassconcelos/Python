# Escreva um progrma que leia números inteiros do teclado.
# O programa deve ler os números até que o
# Usuário digite 0 (zero)
# No final da execução, exiba a quantidade de números digitados,
# assim como a soma das aritméticas 

soma = 0
quantidade = 0

while True:
    num = int(input("Digite um número (0 para sair)"))
    if num == 0:
        break
    soma += num 
    quantidade += 1

    if quantidade >0:
        media = soma / quantidade
        print(f"Quantidade de números digitados: {quantidade}")
        print(f"Soma de números digitados: {soma}")
        print(f"Média aritmética: {media} ")
    else:
        print("Nenhum número foi digitado")