import os.path
import socket
import sys
from thread import *
from threading import Thread
import sqlite3

class client_thread(Thread):

    def __init__(self, addr, c):
        Thread.__init__(self)
        self.addr = addr
        self.c = c

    def run(self):
        while True:
            auth_server(self.addr, self.c)

def auth_server(name, c):
    input = c.recv(2048)
    print "Server started"
    usrname = c.recv(2048)
    pwd = c.recv(2048)
    print usrname + pwd + input

    connection = sqlite3.connect('authentication.db')
    print "Opened database"
    value = ''
    q = ''
    i = 0

    if input == '1':
        cursor = connection.execute("SELECT password from data WHERE username = (?)", (username,))
        for row in cursor:
            q = row[0]
        if q == pwd:
            value = 'true'
        else:
            value = 'false'
    if input == '2':
        cursor = connection.execute("SELECT username from data")
        for row in cursor:
            u = row[0]
            if u == usrname:
                i = 1
        if i != 0:
            value = 'exists'
        else:
            cursor = connection.execute("INSERT INTO data VALUES (?, ?)", (username, password))
            connection.commit()
            value = 'true'
    c.send(value.encode())

def Main():
    host = 'localhost'
    port = 5013
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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