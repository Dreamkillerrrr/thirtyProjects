# server.py
# created by yub at 2019/12/12
import socket
s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))

s.listen(5)

while True:
    msg = 'hello,yub'
    c, address = s.accept()
    print('连接地址为：', address)
    c.send(msg.encode('utf-8'))
    c.close()

