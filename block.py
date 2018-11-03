#encoding:utf-8
import time
import hashlib
import proofofwork as pfw

class Block(object):
    def __init__(self, data, prevBlockHash):
        self.Timestamp = time.time()
        self.Data = data
        self.PrevBlockHash = prevBlockHash  #string
        self.Nonce = 0
        self.Hash = ''
        self.Validate = False
        self.SetHash()
    
    def SetHash(self):  #TODO:builtin
        proofofwork = pfw.ProofOfWork(self)
        nonce, Hash = proofofwork.Run()
        self.Hash = Hash
        self.Nonce = nonce
        self.Validate = proofofwork.Validate()
           
    def __str__(self):
        return "PrevBlockHash: " + self.PrevBlockHash + "\n" + "Data: " + self.Data + "\n" + "Hash: " + self.Hash + "\n" + "Nonce: " + str(self.Nonce) + "\n" + "Validate: " + str(self.Validate) + "\n"
    
    

