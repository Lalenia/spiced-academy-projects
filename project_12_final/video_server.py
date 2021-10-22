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
#ip = "192.168.0.11 "
hostIP = socket.gethostbyname(socket.gethostname())
#print(hostIP)
 
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
        
host = socket.gethostname() 
s.bind((hostIP,port))

while True:
    x = s.recvfrom(100000000)
    clinetip = x[1][0]
    data = x[0]
    print(data)
    data = pickle.loads(data)
    print(type(data))
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    cv2.imshow('my pic', data)
    if cv2.waitKey(10) == 13:
        break
cv2.destroyAllWindows()


#have to run before :python -m http.server

'''import SimpleHTTPServer, SocketServer
PORT = 8000
httpd = SocketServer.TCPServer(("", PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.allow_reuse_address = True
print "Serving at port", PORT
httpd.serve_forever()'''
