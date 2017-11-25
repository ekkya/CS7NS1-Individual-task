import os.path
import socket
import select
import sys
from thread import *
import threading

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 5001            # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
path = "/home/ekkya/CS7NS1-Individual-task/Dummy"
dir = os.listdir(path)
print dir
#while True:
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
#c.send(str(dir))
print "Waiting for reply from client"
a = c.recv(1024)
print a
remove = a[1:-1]
print remove
h = remove.split(", ")
h1 = h[0].replace("'", "")
print h1
f1 = h[1]
print f1
if f1 == "'r'":
       print "Read"
       f = open(h1)
       l = f.read(1024)
       while (l):
              c.send(l)
              print('Sent ',repr(l))
              l = f.read(1024)
       f.close()
       print "File was sent"
elif f1 == "'a'":
       a1 = c.recv(1024)
       print a1
       f = open(h1, 'a')
       #l1 = f.read(1024)
       l = f.write(a1)
       print "File Modified"
       f.close()

else:
       print "Failed to Read"
c.close()                # Close the connection