import random

# Inicializa as pontuações do usuário e do computador.
pontos_usuario = 0
pontos_computador = 0

# Define as opções para o jogo: R (Pedra), T (Tesoura), P (Papel).
opcoes = {"r": "Pedra", "t": "Tesoura", "p": "Papel"}

# Loop principal do jogo.
while True:
    # Solicita ao usuário que faça uma escolha (R/T/P) ou Q para sair.
    escolha_usuario = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair: ").lower()

    # Se o usuário escolher 'q', o loop é encerrado.
    if escolha_usuario == 'q':
        break

    # Se a escolha do usuário não estiver nas opções válidas, o loop continua.
    if escolha_usuario not in opcoes:
        print("Escolha inválida. Tente novamente.")
        continue

    # O computador faz uma escolha aleatória entre R, T e P.
    escolha_computador = random.choice(list(opcoes.keys()))

    # Exibe as escolhas do usuário e do computador.
    print(f"Você escolheu {opcoes[escolha_usuario]}")
    print(f"O computador escolheu {opcoes[escolha_computador]}")

    # Avalia o resultado do jogo e atualiza as pontuações.
    if escolha_usuario == escolha_computador:
        print("Empate!")

    elif (escolha_usuario == "r" and escolha_computador == "t") or \
         (escolha_usuario == "p" and escolha_computador == "r") or \
         (escolha_usuario == "t" and escolha_computador == "p"):
        print("Você ganhou!")
        pontos_usuario += 1

    else:
        print("Você perdeu!")
        pontos_computador += 1

# Exibe as pontuações finais.
print(f"\nSua pontuação: {pontos_usuario}")
print(f"Pontuação do Computador: {pontos_computador}")

# Determina o resultado final com base nas pontuações.
if pontos_computador > pontos_usuario:
    print("Derrota!!!!")
elif pontos_computador == pontos_usuario:
    print("Empate")
else:
    print("Vitória!!")
