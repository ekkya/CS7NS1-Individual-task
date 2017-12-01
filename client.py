import socket               # Import socket module
import pickle

def directory():
    input = raw_input("Welcome to the Directory. Type n for new file or Type e for existing file")
    if input == 'n':
        file_name = raw_input("Enter file name")
        s_dr.send(file_name.encode())
        info = raw_input("Write data into file: ")
        s_dr.send(info.encode())

        data = (s_dr.recv(2048)).decode()
        files = pickle.loads(data)
        print files

    if files:
        f_name = raw_input("Enter File Name, type exit to quit: ")
        f_name.encode()
        s_dr.send(f_name.encode())
        data = s_dr.recv(2048)
        data1 = data.decode()
        print data1
    f_name1 = raw_input("OK. What do you want to do now? Contact fileserver, type yes")
    if f_name1 == 'yes':
        #data2 = 'exit'
        #s_dr.send(data2.encode())
        fileserver(f_name)
    elif f_name1 == 'exit':
        f_name1.encode()
        s_dr.send(f_name1.encode())
        print "Client exit"
    #s_dr.close()

def fileserver(f):
    mode = ['r', 'a']
    status = lock(f)
    if status == 'locked':
        p = raw_input("File is locked. File only available in read mode. Type yes to continue or exit to quit")
        if p == 'yes':
            x = mode[0]
            g = [f, x]
            s_fs.send(str(g))
            with open('received_file', 'wb') as f1:
                print 'file opened'
                while True:
                    print('receiving data...')
                    data = s_fs.recv(1024)
                    print('data=%s', (data))
                    if not data:
                        break
                    # write data to a file
                    f1.write(data)
                f1.close()
    else:
        x = raw_input("File is Unlocked. Read and Write available. What do you want to do? Type r for read or type a for appending the file")
        if x == mode[0]:
            g = [f, x]
            s_fs.send(str(g))
            with open('received_file', 'wb') as f1:
                print 'file opened'
                while True:
                    print('receiving data...')
                    data = s_fs.recv(1024)
                    print('data=%s', (data))
                    if not data:
                        break
                    # write data to a file
                    f1.write(data)
                f1.close()
        elif x == mode[1]:
            g = [f, mode[1]]
            s_fs.send(str(g))
            s_ls.send((str(g[0]).encode()))
            #status = s_ls.recv(1024)
            #print status
            data1 = raw_input("What do you want to write to file?" + str(g[0]))
            print "Modified content: " + str(data1)
            s_fs.send(data1)
            print "Changes sent!"
            s_ls.send("done".encode())
        #s_fs.close                     # Close the socket when done
        w = raw_input("OK. Type b to return to directory server. Press e to quit")
        if w == 'b':
            directory()
        elif w == 'e':
            s_dr.send(w.encode())
            s_fs.send(w.encode())
            s_ls.send(w.encode())

def lock(file_name):
    s_ls.send(file_name.encode())
    status = s_ls.recv(1024)
    print "Status of file: " + str(status)
    #updated_status = s_ls.recv(1024)

    return status
    #return updated_status

if __name__ == '__main__':
    host = 'localhost'
    port_dr = 5011
    s_dr = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s_dr.connect((host, port_dr))

    s_fs = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # Create a socket object
    port_fs = 5012  # Reserve a port for your service.
    s_fs.connect((host, port_fs))

    s_ls = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # Create a socket object
    port_ls = 5007
    s_ls.connect((host, port_ls))

    directory()
    #fileserver()
