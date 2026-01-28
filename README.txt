• Observações:

1) O código pode ser rodado tanto no sistema operacional Windows quanto Linux, desde que tenha a linguagem de programação Python instalada;
2) Para gerar um certificado digital, é necessário instalar o OpenSSL;
3) Para rodar o código, primeiramente rode o servidor com o comando: python servidor.py. Em seguida, rode o cliente com o comando: python cliente.py.


• Comando para gerar um certificado:

openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -config openssl.cnf
