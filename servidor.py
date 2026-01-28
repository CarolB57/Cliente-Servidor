import http.server
import ssl
import sys
import urllib.parse

HOST = "0.0.0.0" # Aceita conexões de qualquer IP
PORT = 65432 # Porta TCP do servidor


class CustomHandler(http.server.BaseHTTPRequestHandler): # Classe para processamento de requisições HTTP
    def do_GET(self):

        query_components = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query) # Extrair a mensagem enviada como parâmetro na URL
        mensagem = query_components.get("message", [""])[0]  # Extrair a mensagem enviada
        
        if not mensagem or mensagem == "/": # Evitar a exibição da listagem de arquivos do diretório
            mensagem = "Nenhuma mensagem recebida!"

        print(f"Mensagem recebida: {mensagem}")
        
        if mensagem.lower() == "sair":
            print("Comando 'sair' emitido.")
            self.send_response(200) # Requisição bem sucedida
            self.send_header("Content-type", "text/plain; charset=utf-8") # Definição do cabeçalho HTTP na resposta como um plaintext
            self.end_headers() # Finalização dos cabeçalhos
            self.wfile.write(b"Encerrar servidor.\n") # Envia a resposta ao cliente

            sys.exit(0) # Encerra o servidor
            return

        # Resposta ao cliente
        self.send_response(200) # Requisição bem sucedida
        self.send_header("Content-type", "text/plain; charset=utf-8") # Definição do cabeçalho HTTP na resposta como um plaintext
        self.end_headers() # Finalização dos cabeçalhos
        self.wfile.write(f"Servidor recebe: {mensagem}".encode("utf-8"))  # Envia ao cliente uma mensagem formatada em bytes

    def log_message(self, format, *args): # Retirar as mensagens dos logs ao mostrar as mensagens recebidas na tela
        return



# Configurar o servidor HTTPS
endereco_servidor = (HOST, PORT)
httpd = http.server.HTTPServer(endereco_servidor, CustomHandler) # Criação de um servidor HTTP que usará a classe CustomHandler para processar as requisições

# TLS 1.3
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) # Criação de um contexto SSL que define que o servidor utilizará o TLS 1.3 na proteção de conexões
context.minimum_version = ssl.TLSVersion.TLSv1_3 # Garantir o uso da versão 1.3 do TLS
context.load_cert_chain(certfile = "server.crt", keyfile = "server.key") # Carregar o certificado e a chave privada
httpd.socket = context.wrap_socket(httpd.socket, server_side = True) # Associar o socket do servidor ao TLS. Dessa forma, o servidor aceita apenas conexões HTTPS

print(f"Servidor HTTPS em https://{HOST}:{PORT}/")

try:
    httpd.serve_forever() # Servidor HTTP entra em um loop infinito, aguardando e processando requisições até ser interrompido.
except KeyboardInterrupt:
    print("\n Servidor encerrado pelo cliente.")

