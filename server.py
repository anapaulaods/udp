import socket
host = "localhost"
port = 2509

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind((host, port))

print("Servidor UDP iniciado!")

while True:
    dados = udp.recvfrom(1024)
    message = dados[0]
    addr = dados[1]

    print("Mensagem do Cliente: ", message)
    print("IP do Cliente: ", addr)
    
    messageBytes = len(message)
    udp.sendto(str(messageBytes).encode('utf-8'), addr)