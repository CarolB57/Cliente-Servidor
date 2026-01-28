# Implementação Cliente-Servidor HTTPS

O código em questão se baseia na implementação um cliente-servidor que se comunicam através do protocolo HTTPS, criptografado com TLS 1.3.

# Etapas

- O servidor carrega certificado e chave privada; 
- O cliente envia uma requisição GET com mensagem no URL; 
- O servidor processa e extrai a mensagem, emitindo uma resposta; 
- O cliente pode continuar enviando ou encerrar a conexão ('`sair`').

# Segurança:

Garante autenticação do servidor via certificado digital e proteção contra ataques de injeção HTML ao emitir respostas com texto puro.

# Rodar o código

Para rodar o código, primeiramente rode o servidor com o comando: 

```
python servidor.py
```

Em seguida, rode o cliente com o comando: 

```
python cliente.py
```

# Geração do certificado

Rode:

```
openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -config openssl.cnf
```
