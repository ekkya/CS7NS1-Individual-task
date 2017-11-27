import socket
from threading import Thread
import threading
import os

def lock():
    host = 'localhost'
    port = 5006
    s = socket.socket()
    s.bind(('', port))
    s.listen(5)
    c, addr = s.accept()
    x = c.recv(2048)
    print x

    #c.send(x.encode())

    files = {}
    if x in files.keys():
        value = files.get(x)
        c.send(value.encode())
    else:
        files[x] = 'Unlocked'
        print files
        value = files.get(x)
        c.send(value.encode())

if __name__ == '__main__':
    lock()