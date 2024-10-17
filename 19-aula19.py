def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32


def celsius_para_kelvin(c):
    return c + 273.15


def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9


def fahrenheit_para_kelvin(f):
    return ( f - 32) * 5/9 + 273.15


def kelvin_para_celsius(f):
    return K - 273.15


def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32 


def menu():
    print("\nEscolha uma opção de conversão:" )
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Fahrenheit para Celsius")
    print("4. Fahrenheit para Kelvin")
    print("5.  Kelvin para Celsius")
    print("6. Kelvin para Fahrenheit")
    print("0.Sair")


while True:
    menu()
    opcao = int(input("\nDigite a opção desejada: ")