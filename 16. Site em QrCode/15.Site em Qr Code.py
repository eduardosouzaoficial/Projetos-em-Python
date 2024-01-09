import qrcode

def formatar_url(url):
    # Adiciona "https://" à URL se não começar com nenhum protocolo
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url

# Solicita ao usuário que insira a URL do site
site_url = input("Digite o URL do site para o qual você deseja gerar o QR Code: ")

# Formata a URL inserida pelo usuário
site_url = formatar_url(site_url)

# Cria um código QR com a URL formatada
codigo_qr = qrcode.make(site_url)

# Salva a imagem do código QR como um arquivo JPEG
nome_arquivo = "codigo_qr_site.jpg"
codigo_qr.save(nome_arquivo)

# Exibe uma mensagem informando o nome do arquivo gerado
print(f"O código QR para o site {site_url} foi gerado e salvo como '{nome_arquivo}'.")
