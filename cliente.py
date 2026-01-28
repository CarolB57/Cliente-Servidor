import requests

url_servidor = "https://127.0.0.1:65432/" # URL do servidor HTTPS
certificado = "server.crt"  # Caminho do certificado do servidor

while True:
    mensagem = input("Digite uma mensagem (ou 'sair' para encerrar a conexão): ")

    if mensagem.lower() == "sair":
        print("Encerrando conexão com o servidor.")
        resposta = requests.get(f"{url_servidor}?message={mensagem}", verify = certificado) # Enviar uma mensagem via HTTPS para o servidor usando uma requisição GET com validação
                                                                                            # do certificado do servidor
        resposta.encoding = "utf-8"
        print(f"Resposta do servidor: {resposta.text}")
        break

    try:
        resposta = requests.get(f"{url_servidor}?message={mensagem}", verify = certificado) # Usa-se verify = certificado para verificar o certificado do servidor
        print(f"Resposta do servidor: {resposta.text}")

    except requests.exceptions.SSLError as e:
        print(f"Erro SSL: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Erro na conexão: {e}")
