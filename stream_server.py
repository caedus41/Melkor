#!/usr/bin/python 
import socket
import subprocess as _sp

host = 'localhost'
port = 4097

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind((host, port))

serv_sock.listen(5)

while 1:
    (client_sock, addr) = serv_sock.accept()    
    print 'Got connection from %s' % repr(addr)

    # TODO: Do something better with this socket
    # # # # Probably create a new thread to handle it
    client_sock.send('Just sending you junk')
    client_sock.close()
    
