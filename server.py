import socket
s=socket.socket()  #socket creation
print("Socket Created")

s.bind(('localhost',9999))#yahn hm ip address ,socket number dety han
#is case may ipaddress mare local machine ha so mane localhost likh diya


s.listen(4)#how many clients can connect with this
print("Waiting for teh connection")


while True:
    c,addr=s.accept()#ye 2 cheezain return kry ga socket ,address
    name=c.recv(1024).decode()
    print("Connected with address:",addr,name)

    c.send(bytes("Welcome to Ibrar server","utf-8"))

    c.close()


