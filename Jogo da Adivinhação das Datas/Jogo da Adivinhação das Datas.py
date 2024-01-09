import json
import random

# Abre o arquivo JSON que contém palavras e dicas relacionadas a datas
f = open('Palavras.json', encoding="utf8")

# Carrega o conteúdo do arquivo JSON em um dicionário chamado 'Palavras'
Palavras = json.load(f)

# Escolhe aleatoriamente uma palavra do dicionário
choice_c = random.choice(list(Palavras.keys()))

# Imprime mensagem de boas-vindas
print("Ola, seja bem-vindo!")
print("#################################")

# Número máximo de tentativas que o jogador tem para adivinhar a data
n_choices = 5
# Flag indicando se o jogador venceu o jogo
win = False

# Loop principal do jogo
while n_choices > 0 and not win:
    # Imprime a dica associada à palavra escolhida
    print("Dica: " + Palavras[choice_c])

    # Solicita ao jogador uma data no formato DDMMAAAA
    answer_user = input("Data: DDMMAAAA\n")
    print("################## \n")

    # Verifica se a entrada do usuário tem o comprimento correto
    if len(answer_user) != 8:
        print("Erro na entrada. A resposta deve conter 8 digitos.")
        continue

    # Verifica se a entrada do usuário é composta apenas por dígitos
    if answer_user.isdigit():
        check = []  # Lista para armazenar marcadores de acertos e erros
        pontuation = 0  # Pontuação inicial do jogador

        # Compara cada dígito da resposta do jogador com a palavra escolhida
        for i in range(8):
            # Se houver correspondência, adiciona um marcador de acerto
            if answer_user[i] == choice_c[i]:
                check.append("✅")
                pontuation += 1
            else:
                # Se não houver correspondência, adiciona um marcador de erro
                check.append("💢")

        # Imprime a resposta do jogador com marcadores de acertos e erros
        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(answer_user))
        print("#######################\n")

        # Se o jogador acertou todos os dígitos, define a flag de vitória como True
        if pontuation == 8:
            win = True
    else:
        print("Erro na entrada. A resposta deve ser uma data!")
        continue

    # Reduz o número de tentativas restantes
    n_choices -= 1

# Exibe o resultado final
if win:
    print("VITÓRIA!!!")
else:
    print("DERROTA!")
    print("A resposta era: " + choice_c)