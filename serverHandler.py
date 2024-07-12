import socket,os,pickle,time,random
from packet import Packet
from UDPsocket import MySocket

#encapsulate payload,adds seq number ack payload:basically use Packet class
#
class Server():
    def __init__(self,my_ip):
        print('Creating handler for server')
        self.seq_num = 0        
        self.expected_seq_num = 0
        self.your_ip = 0 
        self.my_ip = my_ip
        self.mySocket = self.createSocket(self.my_ip)
        #self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        self.dictionary = {}
    def createSocket(self,port):
        x = MySocket()
        newSocket = x.create()
        boundSocket = x.bind(newSocket, self.my_ip)
        return newSocket

    def getMySocket(self):
        return self.mySocket

    def set_your_ip(self,ip):
        self.your_ip = ip
    
    def get_my_ip(self):
        return self.my_ip

    def getseq_num(self):
        return self.seq_num

    def generateSeq(self):
        seq = random.randrange(100000,999999,50)
        self.seq_num = seq
        return seq

    def createPacket(self, msg, mySeq , yourSeq):        
        packet = Packet(mySeq,msg,True,yourSeq)
        return packet

    #avelorte
    def sendAcks(self, receiverSocket , mySeq, yourSeq):
        packet = Packet(mySeq, 'ack', True, yourSeq)
        ackSender = MySocket()
        ackSender.send_bytes(self.mySocket, receiverSocket, packet)
    
    def listen(self):
        data, ip = self.mySocket.recvfrom(1024)
        if ip in self.dictionary.keys():
            print('\nConnection already established.')
        else:
            print('\nNew client connected')
            recvd_packet = pickle.loads(data)
            seq_num = recvd_packet.seq_num
            my_seq_num = self.generateSeq()
            print('My sequence number for client ip',ip,'is:',my_seq_num)
            self.dictionary[ip] = [seq_num, my_seq_num,0] #client seq,my seq,exp seq
        return data,ip
    
    def handleDuplicates(self, recvd_packet, ip):
        replyPacket = Packet(self.dictionary[ip][1] ,'ack',True, recvd_packet.seq_num + 1)
        self.mySocket.sendto(pickle.dumps(replyPacket),ip)

        # replyPacket = Packet(self.seq_num ,'ack',True, recvd_packet.seq_num + 1)
        # self.mySocket.sendto(pickle.dumps(replyPacket),ip)

    def handleExpectedPacket(self, recvd_packet,ip):
        self.dictionary[ip][1]+=1
        replyPacket = Packet(self.dictionary[ip][1] ,'ack',True,recvd_packet.seq_num + 1)
        self.dictionary[ip][2] = self.dictionary[ip][1] + 1
        self.mySocket.sendto(pickle.dumps(replyPacket),ip)
        # self.seq_num+=1
        # replyPacket = Packet(self.seq_num ,'ack',True,recvd_packet.seq_num + 1)
        # self.expected_seq_num = self.seq_num + 1
        # self.mySocket.sendto(pickle.dumps(replyPacket),ip)
    
    def close(self):
        self.mySocket.close()