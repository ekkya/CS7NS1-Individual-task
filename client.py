import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 11116               # Reserve a port for your service.

s.connect((host, port))
received = s.recv(1024)
print received
remove = received[1:-1]
print remove
h = remove.split(", ")
f = h[2]
print f
mode = ['r', 'w']
print mode[0]
g = [f, mode[0]]
g1 = g[0][1:-1]
print g1
g = [g1, mode[0]]
print g
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
s.close                     # Close the socket when done
