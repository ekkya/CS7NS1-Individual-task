import socket, pickle
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
    f_name = (sock.recv(2048)).decode()
    print f_name
    f = open(f_name, "w+")
    info = (sock.recv(2048)).decode()
    print info
    f.write(info)
    print "File creation complete"
    f.close()

    files = []
    current_working_directory = os.getcwd()
    os.chdir(current_working_directory)
    files = os.listdir(current_working_directory)
    data = pickle.dumps(files)
    sock.send(data)
    file_name = sock.recv(2048)
    file_name1 = 'none'
    while file_name1 != 'e':
        if file_name in files:
            i = files.index(file_name)
            print "Exists"
            #Check with lockserver if file is locked or not
            data = current_working_directory + file_name + ' Size ' + str(
                os.path.getsize(files[i])) + ' Last modified ' + str(os.path.getctime(files[i]))
            print data
            data2 = data.encode()
            sock.send(data2)
        else:
            data1 = 'File does not exist, please try again'
            data1.encode()
            sock.send(data1.encode())
        file_name1 = sock.recv(2048)
    sock.close()

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