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
    f_name1 = 'none'
    file_name = c.recv(1024)
    while f_name1 != 'e':
        #print file_name
        files = {}
        cursor = connection.execute("SELECT file_name, status from files_list")
        i = 0
        for row in cursor:
            #print row[0]
            #print row[1]
            d_f = row[0]
            d_s = row[1]
            if d_f == file_name:
                i = i + 1
                #print file_name
        if i == 0:
            d_f = file_name
            d_s = 'Unlocked'
            cursor = connection.execute("INSERT INTO files_list VALUES (?, ?)", (d_f, d_s))
            connection.commit()
        else:
            print "File Exists"
            cursor = connection.execute("SELECT status from files_list WHERE file_name = (?)", (file_name,))
            for row in cursor:
                d_s = row[0]
        c.send(d_s.encode())

        f_name = c.recv(1024)
        cursor = connection.execute("UPDATE files_list SET status = 'locked' WHERE file_name = (?)", (f_name,))
        connection.commit()
        print "File locked"

        input = c.recv(1024)
        if input == 'done':
            cursor = connection.execute("UPDATE files_list SET status = 'unlocked' WHERE file_name = (?)", (f_name,))
            connection.commit()
        f_name1 = c.recv(1024)
    c.close()

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