import socket,os,pickle,time,random
from packet import Packet

#class clientHandler,serverHandler,main
#client handler : 
class MySocket():
    def __init__(self):
        print('Exiting socket constructor...')
    
    def create(self):
        try:
            my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
        except socket.error:
            print("Oops, something went wrong connecting the socket")
            exit()
    
        return my_socket

    def bind(self, mySocket, port):
        try:
            mySocket.bind(("", port))
        except socket.error:
            print('Unable to bind socket to port ',port)
        return mySocket
        
    def send(self,mySocket,receiverSocket,data):
        try:
            mySocket.sendto(data, receiverSocket)
        except socket.error:
            print('Unable to send packet')

    def send_bytes(self,mySocket, receiverSocket , data):
        try:
            mySocket.sendto(pickle.dumps(data), receiverSocket)
        except socket.error:
            print('Unable to send packet in bytes')

    def receive(self, mySocket, numberOfBytes):
        try:
            data, ip = mySocket.recvfrom(numberOfBytes)
        except socket.error:
            print('Unable to receive packets')

        return data, ip 
    
    def receiveBytes(self, mySocket, receiverSocket, numberOfBytes):
        try:
            data, ip = mySocket.recvfrom(numberOfBytes)
        except socket.error:
            print('Unable to receive packets')

        return pickle.loads(data), ip 
    
    
    #TODO
    #create
    #send
    #receive
    #bind
    #sendBytes