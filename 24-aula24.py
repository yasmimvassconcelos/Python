soma_pares = 0

for numero in range(1, 51):
    if numero % 2 == 0:
        soma_pares += numero

print("A soma dos números pares de 1 a 50 é:", soma_pares)