contador = 0

while contador < 100:
    contador += 1
    
    if contador == 6:
        print("Não vou mostrar o 6.")
        continue  # Interrompe a iteração atual e volta para o início do laço

    if contador == 40:
        print("Não vou mostrar o 40.")
        continue  # Interrompe a iteração atual e volta para o início do laço

    if contador >= 10 and contador <= 27:
        print("Não vou mostrar o", contador)
        continue  # Interrompe a iteração atual e volta para o início do laço

    print(contador)  # Exibe o contador se não cair em nenhum dos casos acima

    if contador == 50:  # Interrompe o loop completamente quando o contador atinge 50
        print("Interrompendo o loop no 50.")
        break  # Sai do laço

print("Acabou")