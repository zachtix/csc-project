import socket

serverip = 'localhost'
port = 7000

while True:
  data = input('What your send? : ')
  server = socket.socket()
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  server.connect((serverip, port))
  server.send(data.encode('utf-8'))

  data_server = server.recv(1024).decode()
  print(data_server)
  server.close()