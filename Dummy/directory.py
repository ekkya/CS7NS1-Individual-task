import socket
from threading import Thread
import threading
import os

def get_list(name, sock):
    current_working_directory = os.getcwd()
    os.chdir(current_working_directory)
    files = []
    data = []
    d1 = []
    files = os.listdir(current_working_directory)
    f_name = sock.recv(2048)
    while f_name != 'exit':
        if f_name in files:
            i = files.index(f_name)
            print "Exists"
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
    port = 5000
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    print "Server Started"
    #while True:
    c, addr = s.accept()
    print "Client Connected IP:" + str(addr)
    t = threading.Thread(target=get_list('get_list', c))
    t.start()


if __name__ == '__main__':
    Main()