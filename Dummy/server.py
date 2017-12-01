import os.path
import socket
import select
import sys
from thread import *
from threading import Thread
import pickle


class client_thread(Thread):

    def __init__(self, addr, c):
        Thread.__init__(self)
        self.addr = addr
        self.c = c

    def run(self):
        while True:
            FileServer(self.addr, self.c)

def FileServer(name, c):
    a1 = 'none'
    a = c.recv(1024)
    while a1 != 'e':
       path = "/home/ekkya/CS7NS1-Individual-task/Dummy"
       dir = os.listdir(path)
       print dir
       print "Waiting for reply from client"
       #a = c.recv(1024)
       print a
       remove = a[1:-1]
       #print remove
       h = remove.split(", ")
       h1 = h[0].replace("'", "")
       #print h1
       f1 = h[1]
       #print f1
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
              l = f.write(a1)
              print "File Modified"
              f.close()

       else:
              print "Failed to Read"
       a1 = c.recv(1024)
    c.close()                # Close the connection

def Main():
    host = 'localhost'
    port = 5012
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('', port))
    s.listen(5)
    print "Server Started"
    while True:
        c, addr = s.accept()
        print "Client Connected IP:" + str(addr)
        Thread = client_thread(addr, c)
        Thread.start()

if __name__ == '__main__':
       Main()
