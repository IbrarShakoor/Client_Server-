import socket
c=socket.socket()


c.connect(('localhost',9999))#Jis ip address or port nujmber su connect krna ho


name=input("Enter the name:")

c.send(bytes(name,'utf-8'))

print(c.recv(1024).decode())#is sy hmy jo cliunet sy mil rha ho wo recieve kr skty han
