import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 11117               # Reserve a port for your service.

s.connect((host, port))
received = s.recv(1024)
print received
remove = received[1:-1]
print remove
h = remove.split(", ")
f = h[2]
print f
mode = ['r', 'a']
print mode[0]
g = [f, mode[0]]
g1 = g[0][1:-1]
print g1
g = [g1, mode[0]]
print g
x = raw_input("What do you want to do?")

if x == mode[0] :
    g = [g1, mode[0]]
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
    g = [g1, mode[1]]
    s.send(str(g))
    data1 = raw_input("What do you want to write to file" + str(g1))
    print "Modified content: " + str(data1)
    s.send(data1)
    print "Changes sent!"

s.close                     # Close the socket when done
