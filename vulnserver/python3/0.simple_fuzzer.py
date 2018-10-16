import socket

dest = '127.0.0.1'
dport = 9999
commands = ["HELP","STATS ","RTIME ","LTIME ","SRUN ","TRUN ","GMON ","GDOG ","KSTET ","GTER ","HTER ","LTER ","KSTAN "]
buff = ["A"]
counter = 50

while len(buff) <= 80:
     buff.append("A"*counter)
     counter = counter+50

for command in commands:
     for chars in buff:
          print("Fuzzing " + command + " " + str(len(chars)))
          s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          s.connect((dest, dport))
          s.recv(100)
          s.send(command + chars)
          s.close()
