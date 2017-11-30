import socket
from threading import Thread
import threading
import os

class client_thread(Thread):

    def __init__(self, addr, c):
        Thread.__init__(self)
        self.addr = addr
        self.c = c

    def run(self):
        while True:
            get_list(self.addr, self.c)


def get_list(name, sock):
    current_working_directory = os.getcwd()
    os.chdir(current_working_directory)
    files = []
    d1 = []
    files = os.listdir(current_working_directory)
    f_name = sock.recv(2048)
    while f_name != 'exit':
        if f_name in files:
            i = files.index(f_name)
            print "Exists"
            #Check with lockserver if file is locked or not
            data = current_working_directory + f_name + ' Size ' + str(
                os.path.getsize(files[i])) + ' Last modified ' + str(os.path.getctime(files[i]))
            print data
            data2 = data.encode()
            sock.send(data2)
        else:
            data1 = 'File does not exist, please try again'
            data1.encode()
            sock.send(data1.encode())
        f_name = sock.recv(2048)

def Main():
    host = 'localhost'
    port = 5011
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