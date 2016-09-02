import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8080))
message = 'pie'
sock.send(message)
response = sock.recv(1024)
print response
sock.close()
