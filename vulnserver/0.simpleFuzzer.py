import socket

dest = '127.0.0.1'
dport = 9999

# Create and array of buffers, 1 to 4000 incrementing by 50
buffer=["A"]
counter=50

while len(buffer) <= 80:
     buffer.append("A"*counter)
     counter = counter+50


commands=["HELP","STATS ","RTIME ","LTIME ","SRUN ","TRUN ","GMON ","GDOG ","KSTET ","GTER ","HTER ","LTER ","KSTAN "] # As help indicates, a period may be needed after the space in these commands to successfully fuzz certain aspects of vulnserver

for command in commands:
     for chars in buffer:
          print "Fuzzing " + command + " " + str(len(chars))
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((dest, dport))
          s.recv(100)
          s.send(command + chars)
          s.close()
