import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import socket
import cv2
import numpy
import pickle

import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 10000000)
hostIP = socket.gethostbyname(socket.gethostname())
port= 1024
while True:
    try:
        httpd = socketserver.TCPServer(('', port), Handler)
        print ('Serving on port', port)
        httpd.serve_forever()
    except socketserver.socket.error as exc:
        if exc.args[0] != 48:
            raise
        print ('Port', port, 'already in use')
        port += 1
    else:
        break

cap = cv2.VideoCapture(0)
while True:
    ret,photo = cap.read()
    cv2.imshow('my pic', photo)
    ret, buffer = cv2.imencode(".jpg", photo, [int(cv2.IMWRITE_JPEG_QUALITY),30])
    x_as_bytes = pickle.dumps(buffer)
    s.sendto(x_as_bytes,(serverip , serverport))
    if cv2.waitKey(10) == 13:
        break
  
cv2.destroyAllWindows()
cap.release()


