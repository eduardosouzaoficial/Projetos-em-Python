# Mensagem de boas-vindas ao usuário
print("Seja muito bem-vindo ao quiz sobre Tecnologia do Eduardo!")

# Pergunta se o usuário quer começar o quiz
pergunta_user = input("Quer começar? (S/N) ").strip().upper()

# Se a resposta não for "S" (sim), encerra o programa
if pergunta_user != "S":
    quit()

# Inicializa a pontuação do jogador
score = 0

# Mensagem indicando o início do quiz
print("Começando...")

# Pergunta 1
print("1. Quem é o fundador da Microsoft? \n (A) Steve Jobs \n (B) Bill Gates \n (C) Mark Zuckerberg \n (D) Elon Musk \n")
pergunta_1 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_1 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 2
print("2. Quem é o criador da World Wide Web (WWW)? \n (A) Tim Berners-Lee \n (B) Larry Page \n (C) Mark Andreessen \n (D) Jeff Bezos \n")
pergunta_2 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_2 == "A":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 3
print("3. Qual é a linguagem de programação conhecida por seu uso de indentação significativa? \n (A) Java \n (B) C++ \n (C) Python \n (D) Ruby \n")
pergunta_3 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_3 == "C":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 4
print("4. Qual empresa é responsável pelo desenvolvimento do sistema operacional Windows? \n (A) Apple \n (B) Microsoft \n (C) Google \n (D) Linux Foundation \n")
pergunta_4 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_4 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 5
print("5. Quem é o co-fundador da Apple Inc.? \n (A) Jeff Bezos \n (B) Bill Gates \n (C) Steve Jobs \n (D) Tim Cook \n")
pergunta_5 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_5 == "C":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 6
print("6. Qual é um sistema operacional de código aberto? \n (A) Windows \n (B) macOS \n (C) Linux \n (D) Android \n")
pergunta_6 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_6 == "C":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 7
print("7. Quem é o criador do Facebook? \n (A) Mark Zuckerberg \n (B) Jeff Bezos \n (C) Elon Musk \n (D) Larry Page \n")
pergunta_7 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_7 == "A":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 8
print("8. Qual empresa desenvolveu a linguagem de programação Java? \n (A) Microsoft \n (B) Sun Microsystems \n (C) IBM \n (D) Google \n")
pergunta_8 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_8 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 9
print("9. Qual empresa é conhecida por seus carros elétricos? \n (A) Ford \n (B) Tesla \n (C) Chevrolet \n (D) Toyota \n")
pergunta_9 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_9 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 10
print("10. Qual é a linguagem de programação frequentemente usada para desenvolvimento web? \n (A) Java \n (B) C++ \n (C) Python \n (D) JavaScript \n")
pergunta_10 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_10 == "D":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

print("11. O que significa a sigla HTML? \n (A) HyperText Markup Language \n (B) High-level Text Management Language \n (C) Hyperlink and Text Markup Language \n (D) HyperTransfer Text Management Language \n")
pergunta_11 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_11 == "A":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 12
print("12. Qual é o sistema operacional desenvolvido pela Apple Inc.? \n (A) Windows \n (B) macOS \n (C) Linux \n (D) Android \n")
pergunta_12 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_12 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 13
print("13. Quem é o co-fundador da Microsoft? \n (A) Steve Jobs \n (B) Bill Gates \n (C) Mark Zuckerberg \n (D) Paul Allen \n")
pergunta_13 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_13 == "D":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 14
print("14. O que significa a sigla CSS em desenvolvimento web? \n (A) Computer Style Sheets \n (B) Cascading Style Sheets \n (C) Creative Style Sheets \n (D) Colorful Style Sheets \n")
pergunta_14 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_14 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 15
print("15. Qual linguagem de programação é conhecida por ser orientada a objetos e criada pela Sun Microsystems? \n (A) C++ \n (B) Java \n (C) Python \n (D) Ruby \n")
pergunta_15 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_15 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 16
print("16. Quem é o CEO da Tesla? \n (A) Elon Musk \n (B) Jeff Bezos \n (C) Tim Cook \n (D) Mark Zuckerberg \n")
pergunta_16 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_16 == "A":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 17
print("17. Qual é a principal função do protocolo HTTP em um contexto web? \n (A) Transferência de arquivos \n (B) Compartilhamento de dados \n (C) Comunicação segura \n (D) Transferência de hipertexto \n")
pergunta_17 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_17 == "D":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 18
print("18. Qual é o sistema operacional de código aberto baseado no kernel Linux? \n (A) Windows \n (B) macOS \n (C) Ubuntu \n (D) Android \n")
pergunta_18 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_18 == "C":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 19
print("19. Quem é o co-fundador da empresa de computadores Apple Inc.? \n (A) Jeff Bezos \n (B) Steve Jobs \n (C) Bill Gates \n (D) Tim Cook \n")
pergunta_19 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_19 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 20
print("20. Qual é o significado da sigla SQL em bancos de dados? \n (A) System Query Language \n (B) Structured Query Language \n (C) Simple Query Language \n (D) Sequential Query Language \n")
pergunta_20 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_20 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 21
print("21. Qual é o navegador de internet desenvolvido pela Google? \n (A) Firefox \n (B) Safari \n (C) Chrome \n (D) Edge \n")
pergunta_21 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_21 == "C":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 22
print("22. Em programação, o que é um 'loop'?\n (A) Um erro crítico \n (B) Uma estrutura de controle de fluxo \n (C) Um tipo de variável \n (D) Um tipo de dado \n")
pergunta_22 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_22 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 23
print("23. Qual é a linguagem de programação usada para criar aplicativos Android? \n (A) Swift \n (B) Kotlin \n (C) Java \n (D) C++ \n")
pergunta_23 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_23 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 24
print("24. O que significa a sigla API em desenvolvimento de software? \n (A) Automated Programming Interface \n (B) Application Programming Interface \n (C) Advanced Program Integration \n (D) Automated Process Integration \n")
pergunta_24 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_24 == "B":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Pergunta 25
print("25. Qual é o termo usado para descrever a prática de testar um programa ou sistema por meio da simulação de situações do mundo real? \n (A) Teste de Estresse \n (B) Teste de Usabilidade \n (C) Teste de Integração \n (D) Teste de Campo \n")
pergunta_25 = input("Resposta: ").strip().upper()

# Verifica se a resposta está correta e atualiza a pontuação
if pergunta_25 == "A":
    print("Correto!")
    score += 1
else:
    print("Incorreto!")

# Exibe a mensagem de encerramento do quiz, incluindo a pontuação do jogador
print(f"Quiz acabou... Pontuação: {score}/25")  # Atualize o número total de perguntas

# ...

# Exibe a mensagem de encerramento do quiz, incluindo a pontuação do jogador
print(f"Quiz acabou... Pontuação: {score}/25")  # Atualize o número total de perguntas


# Mostra as respostas incorretas e fornece as respostas corretas
if score < 25:
    # Pergunta 1
    print("\nRespostas Incorretas:")
    if pergunta_1 != "B":
        print("1. Quem é o fundador da Microsoft? - Sua resposta:", pergunta_1, "Resposta correta: B")
    # Pergunta 2
    if pergunta_2 != "A":
        print("2. Quem é o criador da World Wide Web (WWW)? - Sua resposta:", pergunta_2, "Resposta correta: A")
    # Pergunta 3
    if pergunta_3 != "C":
        print("3. Qual é a linguagem de programação conhecida por seu uso de indentação significativa? - Sua resposta:",
              pergunta_3, "Resposta correta: C")
    # Pergunta 4
    if pergunta_4 != "B":
        print("4. Qual empresa é responsável pelo desenvolvimento do sistema operacional Windows? - Sua resposta:",
                  pergunta_4, "Resposta correta: B")

    # Pergunta 5
    if pergunta_5 != "C":
        print("5. Quem é o co-fundador da Apple Inc.? - Sua resposta:", pergunta_5, "Resposta correta: C")

    # Pergunta 6
    if pergunta_6 != "C":
        print("6. Qual é um sistema operacional de código aberto? - Sua resposta:", pergunta_6,
                  "Resposta correta: C")

    # Pergunta 7
    if pergunta_7 != "A":
        print("7. Quem é o criador do Facebook? - Sua resposta:", pergunta_7, "Resposta correta: A")

    # Pergunta 8
    if pergunta_8 != "B":
        print("8. Qual empresa desenvolveu a linguagem de programação Java? - Sua resposta:", pergunta_8,
                  "Resposta correta: B")

    # Pergunta 9
    if pergunta_9 != "B":
        print("9. Qual empresa é conhecida por seus carros elétricos? - Sua resposta:", pergunta_9,
                  "Resposta correta: B")

    # Pergunta 10
    if pergunta_10 != "D":
        print(
                "10. Qual é a linguagem de programação frequentemente usada para desenvolvimento web? - Sua resposta:",
                pergunta_10, "Resposta correta: D")

    # Pergunta 11
    if pergunta_11 != "A":
        print("11. O que significa a sigla HTML? - Sua resposta:", pergunta_11, "Resposta correta: A")

    # Pergunta 12
    if pergunta_12 != "B":
        print("12. Qual é o sistema operacional desenvolvido pela Apple Inc.? - Sua resposta:", pergunta_12,
                  "Resposta correta: B")

    # Pergunta 13
    if pergunta_13 != "D":
        print("13. Quem é o co-fundador da Microsoft? - Sua resposta:", pergunta_13, "Resposta correta: D")

    # Pergunta 14
    if pergunta_14 != "B":
        print("14. O que significa a sigla CSS em desenvolvimento web? - Sua resposta:", pergunta_14,
                  "Resposta correta: B")

    # Pergunta 15
    if pergunta_15 != "B":
        print("15. Qual linguagem de programação é conhecida por ser orientada a objetos e criada pela Sun Microsystems? - Sua resposta:",
                pergunta_15, "Resposta correta: B")
    # Pergunta 15
    if pergunta_16 != "A":
        print("16. Quem é o CEO da Tesla? - Sua resposta:", pergunta_16, "Resposta correta: A")

    # Pergunta 17
    if pergunta_17 != "D":
        print("17. Qual é a principal função do protocolo HTTP em um contexto web? - Sua resposta:", pergunta_17,
                  "Resposta correta: D")

    # Pergunta 18
    if pergunta_18 != "C":
        print("18. Qual é o sistema operacional de código aberto baseado no kernel Linux? - Sua resposta:",
                  pergunta_18, "Resposta correta: C")

    # Pergunta 19
    if pergunta_19 != "B":
        print("19. Quem é o co-fundador da empresa de computadores Apple Inc.? - Sua resposta:", pergunta_19,
                  "Resposta correta: B")

    # Pergunta 20
    if pergunta_20 != "B":
        print("20. Qual é o significado da sigla SQL em bancos de dados? - Sua resposta:", pergunta_20,
                  "Resposta correta: B")

    # Pergunta 21
    if pergunta_21 != "C":
        print("21. Qual é o navegador de internet desenvolvido pela Google? - Sua resposta:", pergunta_21,
                  "Resposta correta: C")

    # Pergunta 22
    if pergunta_22 != "B":
        print("22. Em programação, o que é um 'loop'? - Sua resposta:", pergunta_22, "Resposta correta: B")

    # Pergunta 23
    if pergunta_23 != "B":
        print("23. Qual é a linguagem de programação usada para criar aplicativos Android? - Sua resposta:",
                  pergunta_23, "Resposta correta: B")

    # Pergunta 24
    if pergunta_24 != "B":
        print("24. O que significa a sigla API em desenvolvimento de software? - Sua resposta:", pergunta_24, "Resposta correta: B")
    # Pergunta 24
    if pergunta_25 != "A":
        print("25. Qual é o termo usado para descrever a prática de testar um programa ou sistema por meio da simulação de situações do mundo real? - Sua resposta: ", pergunta_25, " Resposta correta: A")

    print("\nRespostas Corretas:")
    
    print("1. B, 2. A, 3. C, 4. B, 5. C, 6. C, 7. A, 8. B, 9. B, 10. D, 11. A, 12. B, 13. D, 14. B, 15. B, 16. A, 17. D, 18. C, 19. B, 20. B, 21. C, 22. B, 23. B, 24. B, 25. A")

    # Mensagem de incentivo
    print("\nBom trabalho! Continue estudando e se aprimorando em tecnologia!")






