import time

# Solicita ao usuário para digitar o tempo em segundos
t = input("Digite o tempo (em segundos): ")

# Verifica se a entrada do usuário é um número inteiro
if t.isdigit():
    t = int(t)
else:
    # Se a entrada não for um número, imprime uma mensagem de erro e encerra o programa
    print("Entrada inválida!")
    quit()

# Converte o tempo total em minutos e segundos e exibe a contagem regressiva
while t:
    minutes, seconds = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    t = t - 1

# Quando o tempo atinge zero, imprime uma mensagem indicando que o tempo acabou
print("TEMPO ACABOU!!!!")
