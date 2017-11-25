import socket               # Import socket module

def directory():
    host = 'localhost'
    port = 5000
    s = socket.socket()
    s.connect((host, port))
    print "Connection Established with Directory server"
    f_name = raw_input("Enter File Name, type exit to quit: ")
    f_name.encode()
    s.send(f_name.encode())
    data = s.recv(2048)
    data1 = data.decode()
    print data1
    f_name1 = raw_input("OK. What do you want to do now? Contact fileserver type yes, type new for directory servicer or type exit to quit")
    if f_name1 == 'yes':
        data2 = 'exit'
        s.send(data2.encode())
        fileserver(f_name)
    elif f_name1 == 'exit':
        f_name1.encode()
        s.send(f_name1.encode())
    elif f_name1 == 'new':
        f_name = raw_input("Enter File Name, type exit to quit: ")
        f_name.encode()
        s.send(f_name.encode())
        data = s.recv(2048)
        data1 = data.decode()
        print data1
    s.close()

def fileserver(f):
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 5001               # Reserve a port for your service.

    s.connect((host, port))
    #received = s.recv(2048)
    #print received
    #remove = received[1:-1]
    #print remove
    #h = remove.split(", ")
    #f = h[2]
    #print f
    mode = ['r', 'a']
    #print mode[0]
    #g = [f, mode[0]]
    #g1 = g[0][1:-1]
    #print g1
    #g = [g1, mode[0]]
    #print g
    x = raw_input("What do you want to do? Type r for read or type a for appending the file")

    if x == mode[0] :
        g = [f, mode[0]]
        s.send(str(g))
        with open('received_file', 'wb') as f1:
            print 'file opened'
            while True:
                print('receiving data...')
                data = s.recv(1024)
                print('data=%s', (data))
                if not data:
                    break
                # write data to a file
                f1.write(data)
            f1.close()
    elif x == mode[1]:
        g = [f, mode[1]]
        s.send(str(g))
        data1 = raw_input("What do you want to write to file" + str(g1))
        print "Modified content: " + str(data1)
        s.send(data1)
        print "Changes sent!"

    s.close                     # Close the socket when done

if __name__ == '__main__':
    directory()
    #fileserver()
