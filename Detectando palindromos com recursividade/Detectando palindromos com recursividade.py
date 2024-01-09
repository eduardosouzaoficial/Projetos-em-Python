import math

# Função para verificar se uma palavra é um palíndromo (versão iterativa)
def eh_palindromo(palavra):
    j = len(palavra) - 1
    resultado = 0

    # Loop percorrendo a palavra da esquerda para a direita
    for i in range(len(palavra)):
        if palavra[i] == palavra[j]:
            resultado += 1
        if i >= j:
            break
        j = j - 1

    # Verifica se o número de caracteres correspondentes é igual à metade do comprimento da palavra
    if resultado == math.ceil(len(palavra) / 2):
        return True
    else:
        return False

# Função para verificar se uma palavra é um palíndromo (versão recursiva)
def eh_palindromo_recursivo(palavra):
    # Caso base: uma palavra de comprimento 1 ou 0 é sempre um palíndromo
    if len(palavra) <= 1:
        return True
    else:
        # Verifica se o primeiro e o último caractere são iguais
        # e chama recursivamente a função para a substring do meio
        return palavra[0] == palavra[-1] and eh_palindromo_recursivo(palavra[1:-1])

# Solicita ao usuário que insira uma palavra
palavra_usuario = input("Digite uma palavra para verificar se é um palíndromo: ").lower().strip()

# Testa a palavra inserida pelo usuário e exibe os resultados
print(f"\nResultados para a palavra '{palavra_usuario}':")
print("Iterativo:", eh_palindromo(palavra_usuario))
print("Recursivo:", eh_palindromo_recursivo(palavra_usuario))
