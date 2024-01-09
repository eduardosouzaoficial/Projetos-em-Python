import re

def analisar_senha(senha, nome, data_nascimento):
    # Verifica se a senha contém a data de nascimento ou o nome
    if data_nascimento in senha or nome in senha:
        return False, "A senha não pode conter a data de nascimento ou o nome."

    # Verifica a complexidade da senha
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_minuscula = any(c.islower() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_simbolo = bool(re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]", senha))

    if tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo:
        return True, "Senha válida!"
    else:
        return False, "A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula, um número e um símbolo."

def obter_dados_usuario():
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento (formato: DD/MM/AAAA): ")
    return nome, data_nascimento

def main():
    nome, data_nascimento = obter_dados_usuario()

    while True:
        senha = input("Digite a senha desejada: ")

        # Analisa a senha
        senha_valida, mensagem = analisar_senha(senha, nome, data_nascimento)

        # Exibe a mensagem
        print(mensagem)

        # Se a senha for válida, encerra o loop
        if senha_valida:
            break

if __name__ == "__main__":
    main()
