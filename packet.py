#import hashlib

class Packet : 
    seq_num = 0
    payload = 0
    isAck = 0
    msg = ""

    def __init__(self, my_seq_num, payload, isAck, your_seq_num): 
        self.seq_num = my_seq_num
        self.payload = payload
        self.isAck = isAck
        self.your_seq_num = your_seq_num


