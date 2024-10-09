#desvio condicionais
# if/ if-else/ if-elif-else

#if(Condição)
#elif(Condição)
#else

print("Algoritmo do Voto Obrigatório")

nome= input("Qual o seu nome: ")
idade= int(input("Digite a sua idade: "))

if idade >= 18 and idade <= 65:
    print(f"{nome} é maior de idade e pode votar.")
elif idade < 18 or idade >= 65:
    print(f"{nome} Voto opcional")
else:
    print(f"{nome} Voto não autorizado.") 
