#encoding:utf-8
import time
import hashlib

class Block(object):
    def __init__(self, data, prevBlockHash):
        self.Timestamp = time.time()
        self.Data = data
        self.PrevBlockHash = prevBlockHash  #string
        self.Hash = self.SetHash()
    
    def SetHash(self):  #TODO:builtin
        encoder = hashlib.sha256()
        header = self.PrevBlockHash + self.Data + str(self.Timestamp)
        encoder.update(header.encode("utf-8"))
        return encoder.hexdigest()
    
    def __str__(self):
        return "PrevBlockHash: " + self.PrevBlockHash + "\n" + "Data: " + self.Data + "\n" + "Hash: " + self.Hash + "\n"

