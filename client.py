# client.py
# created by yub at 2019/12/12
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
print(s.recv(1024))
s.close()