import io
import socket
import struct
import time
import picamera
import cv2
import numpy as np

client_sock = socket.socket()
client_sock.connect('52.5.38.90', 8080)

conn = client_sock.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        # Sleep to give the camera time to warm up
        time.sleep(2)
        # I'm oh so joyously unsure about this but here's the gist:
        # This PiRGBArray is a subclass of BytesIO, which is what was used in
        # the picamera recipe for capturing to a network stream. Theoretically
        # we're now sending an rgb array to the server
        with picamera.array.PiRGBArray(camera) as camera_stream:
            # Here we record each frame and pass it into the rgb array we just
            # created
            for frame in camera.capture_continuous(camera_stream, format='bgr')
                # Not sure if this array is the same size that would be output
                # from tell on line 22 in which case this won't work
                # We might want to use sys.getsizeof() to determine the size of
                # the image instead
                # conn.write(struct.pack('<L', sys.getsizeof(camera_stream.array)))

                # Either way, here we send the size of the next image to aws
                conn.write(struct.pack('<L', camera_stream.tell()))
                conn.flush()

                # Send the actual image array to the server
                conn.write(camera_stream.array)

                # Send the stream to the start and truncate
                # (not sure if we need truncate)
                camera_stream.seek(0)
                camera_stream.truncate()
finally:
    conn.close()
    client_sock.close()
