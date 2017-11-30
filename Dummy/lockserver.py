import socket
from threading import Thread
import threading
import os.path
import sqlite3


class client_thread(Thread):
    def __init__(self, addr, c):
        Thread.__init__(self)
        self.addr = addr
        self.c = c

    def run(self):
        while True:
            lock(self.addr, self.c)


def lock(name, c):
    connection = sqlite3.connect('test.db')
    print "Database Opened"

    file_name = c.recv(1024)
    print file_name
    files = {}
    cursor = connection.execute("SELECT file_name, status from files")

    for row in cursor:
        print row[0]
        print row[1]
        d_f = row[0]
        d_s = row[1]
        if d_f != file_name:
            print file_name
            d_f = file_name
            d_s = 'Unlocked'
            cursor = connection.execute("INSERT INTO files VALUES (?, ?)", (d_f, d_s))
            connection.commit()

    #if x in files.keys():
     #   value = files.get(x)
      #  c.send(value.encode())
    #else:
     #   files[x] = 'Unlocked'
      #  print files
       # value = files.get(x)
        #c.send(value.encode())
        #v = c.recv(1024)
        #print v
        #if v in files.keys():
         #   files[v] = 'Locked'
          #  print files
            #w = c.recv(1024)
            #if w == "done":
                #files[v] = 'Unlocked'
                #print files

def Main():
    host = 'localhost'
    port = 5007
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