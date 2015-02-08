import socket
import time

host = '127.0.0.1'
port = 8002

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

quitting = False
print "Server Started."
while not quitting:
    try:
        data, addr = s.recvfrom(1024)
        #print "addr = "+addr
        if "Quit" in str(data):
            quitting = True
        curr=""
        for x in str(data):
            if x == ":":
                break
            curr=curr+x

        if addr not in clients:
            clients.append(addr)
        
        print time.ctime(time.time()) + str(addr) + ": :" + str(data)
        
        print curr
        for client in clients:
            if str(client) == str(addr):
                continue;
            s.sendto(data, client)
    except:
        pass
s.close()
