#!/usr/bin/python
import socket 

server_addr = '52.3.38.90'
port = 4097

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

if s is not None: 
    s.connect((server_addr, port))

# TODO: Sending and recving 4096 won't necessarily work all the time
# # # # Fixing this will require a more verbose protocol. do that. 
try: 
    s.send("This will make you happy")
except Exception as e: 
    print 'Something went wrong sending data\n'
    pass

try: 
    data = s.recv(4096)
    print data
except:
    print 'Something went wrong receiving data\n'

s.close()
