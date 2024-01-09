import random
from unidecode import unidecode  # Importa a função unidecode

# Dicionário contendo emojis como chaves e suas respostas como valores
emojis_e_respostas = {
"😱🔪": "Pânico",
    "🐜🐜🐜💤": "FormiguinhaZ",
    "🇺🇸🍰": "American Pie",
    "👩👩‍🦰👩‍🦱👧👖✈️": "Quatro Amigas e um Jeans Viajante",
    "🏠🎈🎈🎈👴👦": "Up – Altas Aventuras",
    "👊💥🐼": "Kung Fu Panda ",
    "🍝🙏👩‍❤️‍👨": "Comer Rezar Amar",
    "👑🦁": "O Rei Leão",
    "👨🕷️": "Homem-Aranha",
    "🔎👻": "Os Caça-Fantasmas",
    "😈👠": "O Diabo Veste Prada",
    "👴💍💍": "O Senhor dos Anéis",
    "🌎🐵🐵🐵": "O Planeta dos Macacos",
    "👻🎤🎼🎶": "O Fantasma da Ópera",
    "👉🍺🍺🚫👰": "Se Beber, Não Case",
    "🧔‍♂️🧔‍♂️🧔‍♂️🧔‍♂️🧔‍♂️🧔‍♂️🧔‍♂️🧔‍♂️🧔‍♂️🧔‍♂️🧔‍♂️🙊": "Onze Homens e um Segredo",
    "🏬🏭🏢🏥😇😇": "Cidade dos Anjos",
    "👧✨➡️👩": "De Repente 30",
    "🚢": "Titanic",
    "💍💍💍💍⚰️": "Quatro Casamentos e Um Funeral",
    "👂🖐️👀👅👃6️⃣": "O Sexto Sentido",
    "🙊👶👶": "O Silêncio dos Inocentes",
    "🗣️👑": "O Discurso do Rei",
    "🤵‍♂️🦇": "Batman",
    "👩‍🦰🥀👹": "A Bela e a Fera",
    "🐝📽️": "Bee Movie",
    "🧑🧑‍🦱👨‍🦱👶": "Três Solteirões e um Bebê",
    "🏝️🧍‍♂️": "O Náufrago",
    "👨‍💼👨‍⚖️👿": "O Advogado do Diabo",
    "🏃.... 🚓": "Corra que a Polícia Vem Aí"
}

def saudacao():
    # Saudação inicial para o jogador
    print("Bem-vindo ao Jogo de Adivinhação de Filmes por Emojis!")
    print("Você verá emojis que representam títulos de filmes. Tente adivinhar o nome do filme correspondente.")
    print("Você pode continuar jogando quantas vezes quiser. Vamos começar!\n")

def normalizar_string(string):
    # Usa a função unidecode para remover acentos e caracteres especiais
    return unidecode(string.lower())

def jogo_emoji():
    saudacao()  # Chama a função de saudação no início do jogo
    acertos = 0  # Inicializa o contador de acertos
    erros = 0    # Inicializa o contador de erros

    while True:
        # Escolhe um emoji aleatório
        emoji_atual = random.choice(list(emojis_e_respostas.keys()))
        print("Adivinhe o filme com base no emoji:")
        print(emoji_atual)

        # Obtém a resposta do usuário
        resposta_usuario = input("Sua resposta: ")
        resposta_correta = emojis_e_respostas[emoji_atual]

        # Normaliza ambas as respostas para comparação sem acentos
        resposta_usuario_normalizada = normalizar_string(resposta_usuario)
        resposta_correta_normalizada = normalizar_string(resposta_correta)

        if resposta_usuario_normalizada == resposta_correta_normalizada:
            # Se a resposta estiver correta, incrementa o contador de acertos
            print("Parabéns! Você acertou!\n")
            acertos += 1
        else:
            # Se a resposta estiver incorreta, incrementa o contador de erros
            print(f"Resposta incorreta. A resposta correta era: {resposta_correta}\n")
            erros += 1

        # Pergunta se o jogador deseja continuar jogando
        continuar = input("Deseja continuar jogando? (s/n): ")
        if continuar.lower() != 's':
            break

    # Exibe o placar final ao encerrar o jogo
    print("\n*** Placar Final ***")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")

    # Pergunta se o jogador deseja reiniciar o jogo
    reiniciar = input("\nDeseja reiniciar o jogo? (s/n): ")
    if reiniciar.lower() == 's':
        jogo_emoji()  # Reinicia o jogo chamando a função principal novamente
    else:
        print("Até a próxima!")

# Inicia o jogo quando o script é executado
if __name__ == "__main__":
    jogo_emoji()
