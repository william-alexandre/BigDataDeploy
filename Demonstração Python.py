import datetime

# Solicita a idade do usuário e garante que seja um número válido (não negativo)
while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade >= 0:
            break
        print("Por gentileza, digite uma idade válida!")
    except ValueError:
        print("Entrada inválida! Digite um número inteiro.")

# Obtém o ano atual automaticamente
ano_atual = datetime.datetime.now().year

# Calcula o ano em que o usuário terá 80 anos
ano_80_anos = ano_atual + (80 - idade)

# Exibe o resultado
print(f"Em {ano_80_anos}, você terá 80 anos.")
