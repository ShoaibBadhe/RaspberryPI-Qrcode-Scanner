import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
s.connect(('127.0.0.1',5000))
print(s.recv(1024))
s.send(r'hello..im client')
