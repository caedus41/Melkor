# This script is heavily based on the recipes from picamera.readthedocs.com
# The script opens a socket and listens for a connection on port 8080 from a
# device streaming video with the following protocol. Video is stramed image
# by image; first, the length in bytes is read, then we read equal to the length
# we just received.
import io
import socket
import struct
import cv2
import numpy as np

serv_sock = socket.socket()
serv_sock.bind(socket.gethostbyname(socket.gethostname()), 8080)
serv_sock.listen(0)

img_stream = io.BytesIO()
conn = serv_sock.accept()[0].makefile('rb')
try: 
    while True:
        # Here we receive the size of the incoming image and unpack the data
        # into a long
        img_len = struct.unpack('<L', conn.read(struct.calcsize('<L')))[0]

        # We may or may not want this - it breaks the loop if there's no data
        #if not img_len:
        #   break

        # Here we read data from the socket until we've read the to the length
        # we received in the last message
        img_stream.write(conn.read(img_len))

        # This is where we would pass the image data to opencv

        # I'm only 95% sure we need this line
        img_stream.seek(0)
except Exception as e:
    print e
finally:
        connection.close()
        serv_sock.close()
