import random
import string

# Função para gerar senhas
def password_generator(len_pass=8):
    # Define as opções de caracteres para a senha
    ascii_options = string.ascii_letters  # letras maiúsculas e minúsculas
    number_options = string.digits  # dígitos de 0 a 9
    punt_options = string.punctuation  # caracteres de pontuação
    options = ascii_options + number_options + punt_options  # todas as opções possíveis

    password_user = ""

    # Loop para construir a senha com a quantidade desejada de caracteres
    for i in range(0, len_pass):
        digit = random.choice(options)  # escolhe aleatoriamente um caractere das opções
        password_user += digit

    return password_user

# Solicita ao usuário a quantidade desejada de dígitos na senha
choice_user = input("Quantos dígitos na senha?")

# Verifica se a entrada do usuário é um número inteiro
if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    # Se a entrada não for um número, imprime uma mensagem de erro e encerra o programa
    print("Entrada inválida!")
    quit()

# Gera a senha com base na escolha do usuário e a imprime
response = password_generator(len_pass=choice_user)
print(f"Senha gerada:\n{response}")
