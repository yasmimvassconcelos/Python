[16:31, 02/10/2024] Yasmim Letícia: # Declaração da função exibirMensagem(nome)
def exibirMensagem(nome, idade):
    print(f"Olá, {nome} com {idade} anos!")


def somar(a, b):
    return a + b


def calcularAreaCirculo(raio):
    area = 3.1415 * raio**2
    return area


# início do meu algoritmo
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
exibirMensagem(nome, idade)   # Exibe a mensagem com o nome do usuário.

# chamando função com retorno
valorA = int(input("Digite o primeiro número:"))
valorB = int(input("Digite o segundo número:"))
resultado = somar(valorA, valorB)
print(f"O resultado da soma = {resultado}")


# Calcular área do círculo
print("Área do círculo!!")
raio = float(input("Digite o valor do raio: "))
area = calcularAreaCirculo(raio)
print(f"A área do círculo : {area:.2f}")
[16:31, 02/10/2024] Samira sami: aula 13-funções.py
[16:38, 02/10/2024] Samira sami: Cigarros = int(input("Digite a quantidade de cigarros fumados por dia:"))
Anos = int(input("Digite quantidade de anos que você fuma:"))

temp_p = anos*365*(Cigarros*10)
dias = (temp_p/60)/24

print (f'Você perdeu: (dias:.1f)dias de vida')