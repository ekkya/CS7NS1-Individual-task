import socket               # Import socket module

def directory():
    print "Connection Established with Directory server"
    f_name = raw_input("Enter File Name, type exit to quit: ")
    f_name.encode()
    s_dr.send(f_name.encode())
    data = s_dr.recv(2048)
    data1 = data.decode()
    print data1
    #lock(f_name)
    f_name1 = raw_input("OK. What do you want to do now? Contact fileserver type yes, type new for directory servicer or type exit to quit")
    if f_name1 == 'yes':
        data2 = 'exit'
        s_dr.send(data2.encode())
        fileserver(f_name)
    elif f_name1 == 'exit':
        f_name1.encode()
        s_dr.send(f_name1.encode())
    elif f_name1 == 'new':
        f_name = raw_input("Enter File Name, type exit to quit: ")
        f_name.encode()
        s_dr.send(f_name.encode())
        data = s_dr.recv(2048)
        data1 = data.decode()
        print data1
    s_dr.close()

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
            data1 = raw_input("What do you want to write to file?" + str(g[0]))
            print "Modified content: " + str(data1)
            s_fs.send(data1)
            print "Changes sent!"

        s_fs.close                     # Close the socket when done


def lock(file_name):
    s_ls.send(file_name.encode())
    status = s_ls.recv(1024)
    print "Status of file: " + str(status)

    return status

if __name__ == '__main__':
    host = 'localhost'
    port_dr = 5004
    s_dr = socket.socket()
    s_dr.connect((host, port_dr))

    s_fs = socket.socket()  # Create a socket object
    port_fs = 5001  # Reserve a port for your service.
    s_fs.connect((host, port_fs))

    s_ls = socket.socket()  # Create a socket object
    port_ls = 5006
    s_ls.connect((host, port_ls))

    directory()
    #fileserver()
