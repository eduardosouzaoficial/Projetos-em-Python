while True:
    # Exibe as opções de operação para o usuário
    print("Escolha a operação:")
    print("1. Converter de Celsius para Kelvin e Fahrenheit")
    print("2. Converter de Fahrenheit para Celsius e Kelvin")
    print("3. Converter de Kelvin para Celsius e Fahrenheit")
    print("4. Sair")

    # Solicita a escolha do usuário
    escolha = input("Digite o número da operação desejada: ")

    # Verifica se o usuário escolheu sair
    if escolha == '4':
        print("Programa encerrado.")
        break

    # Realiza a conversão conforme a escolha do usuário
    if escolha in ['1', '2', '3']:
        # Solicita o valor da temperatura que o usuário deseja converter
        valor = float(input("Digite o valor da temperatura: "))

        # Executa as conversões e exibe os resultados
        if escolha == '1':
            # Converte Celsius para Kelvin e Fahrenheit
            temperatura_em_kelvin = valor + 273.15
            temperatura_em_fahrenheit = (valor * 9/5) + 32
            print(f"{valor} Celsius é igual a {temperatura_em_kelvin:.2f} Kelvin e {temperatura_em_fahrenheit:.2f} Fahrenheit")

        elif escolha == '2':
            # Converte Fahrenheit para Celsius e Kelvin
            temperatura_em_celsius = (valor - 32) * 5/9
            temperatura_em_kelvin = (valor - 32) * 5/9 + 273.15
            print(f"{valor} Fahrenheit é igual a {temperatura_em_celsius:.2f} Celsius e {temperatura_em_kelvin:.2f} Kelvin")

        elif escolha == '3':
            # Converte Kelvin para Celsius e Fahrenheit
            temperatura_em_celsius = valor - 273.15
            temperatura_em_fahrenheit = (valor - 273.15) * 9/5 + 32
            print(f"{valor} Kelvin é igual a {temperatura_em_celsius:.2f} Celsius e {temperatura_em_fahrenheit:.2f} Fahrenheit")

    else:
        # Mensagem de erro se a escolha do usuário for inválida
        print("Opção inválida. Escolha novamente.")
