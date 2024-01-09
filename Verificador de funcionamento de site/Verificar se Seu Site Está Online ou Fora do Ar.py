import requests

def verifica_status_site():
    # Solicita ao usuário o nome do site (somente o domínio)
    dominio = input("Digite o nome do site (por exemplo, google.com): ")

    # Adiciona "https://www." ao domínio para criar a URL completa
    url = f"https://www.{dominio}"

    try:
        # Faz uma solicitação GET para verificar o status do site
        response = requests.get(url, timeout=5)

        # Verifica o código de status da resposta
        if response.status_code == 200:
            print(f"O site {url} está funcionando corretamente (Status: {response.status_code}).")
        else:
            print(f"O site {url} retornou um status inesperado: {response.status_code}")

    except requests.ConnectionError:
        print(f"Não foi possível conectar-se ao site {url}. Verifique sua conexão com a Internet.")
    except requests.Timeout:
        print(f"A solicitação ao site {url} expirou. Verifique a disponibilidade do site.")
    except requests.RequestException as e:
        print(f"Ocorreu um erro ao verificar o site {url}: {e}")

# Exemplo de uso
verifica_status_site()
