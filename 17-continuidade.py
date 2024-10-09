# Ferramenta Continue
# A ferramenta continue no Python vai interromper o loop,
# mas vai dar continuidade a ele.

contador = 0

while contador <= 40:
    contador += 1

    # Verifica se o valor de 'contador' é múltiplo de 4
    if (contador % 4 == 0):
        print("pim") # Se for múltiplo de 4, imprime "pim"
        continue # Interrompe aiterção atual e volta para o ínicio do loop

    # Se o número náo for múltiplo de 4, imprime o valor do contador 
    print(contador)
    #Após otérmino do loop, imprime a mensagem de finalização
    print("Fim dp Programa")