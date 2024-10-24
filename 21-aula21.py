# Desenvolva um programa que solicite ao usuário um valor inteiro,
# referente a um pagamento, e determine a quantidade mínima de cédulas
# necessárias para pagar esse valor.
# Considere as cédulas disponíveis de R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1.
# O programa deve exibir a quantidade de cada tipo de cédula utilizada
# para atingir o valor total.

# Solicita o valor a ser pago
valor = int(input("Digite o valor a pagar: "))

# Lista de cédulas disponíveis
cedulas_disponiveis = [50, 20, 10, 5, 1]

# Variável que armazena o valor restante a ser pago
apagar = valor

# Loop para calcular a quantidade de cédulas de cada valor
for cedula in cedulas_disponiveis:
    quantidade_cedulas = apagar // cedula  # Calcula quantas cédulas de cada valor
    if quantidade_cedulas > 0:  # Se pelo menos uma cédula for usada
        print(f"{quantidade_cedulas} cédula(s) de R${cedula:.2f}")
    apagar = apagar % cedula  # Atualiza o valor restante
    if apagar == 0:  # Se o valor já foi quitado, encerra o loop
        break