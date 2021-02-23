import socket, datetime
host = "localhost"
port = 2509

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tempoInicial = datetime.datetime.now()

message = input("Enviar mensagem: ").encode('utf-8')
udp.sendto(message, (host, port))

dados = udp.recvfrom(1024)
messageBytes = dados[0]
addr = dados[1]

tempoFinal = datetime.datetime.now()
demoraCalculada = tempoFinal - tempoInicial

print("Tempo demorado: ", demoraCalculada)
print("Bytes da mensagem: ", messageBytes)