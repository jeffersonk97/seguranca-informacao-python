import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("\nCliente: Socket  criado com sucesso!")

host = 'localhost'
porta = 5433
mensagem = 'Olá Servidor!'

try:
    print("\nCliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("\nCliente: " + dados)
finally:
    print("\nCliente: Fechando a conexão")
    s.close()
