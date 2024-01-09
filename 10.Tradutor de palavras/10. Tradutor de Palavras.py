from PyDictionary import PyDictionary

# Função para traduzir uma frase do português para o inglês
def traduzir_frase(frase, de_idioma='pt', para_idioma='en'):
    # Instanciar a classe PyDictionary
    dicionario = PyDictionary()

    # Dividir a frase em palavras
    palavras = frase.split()

    # Traduzir cada palavra individualmente
    traducoes = [dicionario.translate(palavra, para_idioma) for palavra in palavras]

    # Juntar as palavras traduzidas para formar a frase traduzida
    frase_traduzida = ' '.join(traducoes)

    return frase_traduzida

# Solicitar ao usuário que insira a frase
frase_a_traduzir = input("Digite a frase a ser traduzida do português para o inglês: ")

# Chamar a função de tradução
frase_traduzida = traduzir_frase(frase_a_traduzir, de_idioma='pt', para_idioma='en')

# Exibir resultados
print("Frase original:", frase_a_traduzir)
print("Frase traduzida:", frase_traduzida)
