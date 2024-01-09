import random

# Exibe uma mensagem de boas-vindas e solicita ao usuário que insira o número máximo para o desafio.
print("Seja muito bem-vindo ao jogo de Adivinhação do Eduardo!")
choice_number = input("Digite o valor máximo para o desafio: ")

# Verifica se o valor inserido é um número. Se sim, converte para inteiro; caso contrário, exibe uma mensagem de erro e encerra o programa.
if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: valor informado não é numérico. Favor execute novamente e informe um número!")
    quit()

# Gera um número aleatório dentro do intervalo de 0 a choice_number.
random_number = random.randint(0, choice_number)

# Inicializa o contador de tentativas.
n_choices = 0

# Inicia um loop que continuará até que o usuário acerte o número gerado aleatoriamente.
while True:
    # Solicita ao usuário que adivinhe o número.
    answer_user = input("Advinhe o número: ")

    # Verifica se a entrada do usuário é um número. Se sim, converte para inteiro; caso contrário, exibe uma mensagem de erro e continua para a próxima iteração do loop.
    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado não é numérico. Favor informe um número!")
        continue

    # Incrementa o número de tentativas.
    n_choices = n_choices + 1

    # Compara a suposição do usuário com o número gerado aleatoriamente e fornece feedback.
    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto, o número randomico é menor que isso..")
    else:
        print("Chutou baixo, o número randomico é maior que isso..")

# Exibe o número de tentativas que o usuário levou para adivinhar o número.
print("N° de tentativas: " + str(n_choices))
