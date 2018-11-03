#encoding:utf-8
import block as b
import hashlib
import sys

targetBits = 24
#maxNonce = sys.maxsize # acctual one 
maxNonce = 20000 # to see the result in a short rime

class ProofOfWork(object):
    def __init__(self, block):
        self.Block = block
        self.target = 1<<targetBits

    def PrepareData(self, nonce):
        data = self.Block.PrevBlockHash + self.Block.Data + str(self.Block.Timestamp) + str(targetBits) + str(nonce)
        return data
    def Run(self):
        nonce = 0
        
        print("Minging the block containing \"%s\"\n" % self.Block.Data)
        while nonce < maxNonce:
            data = self.PrepareData(nonce)
            encoder = hashlib.sha256()
            encoder.update(data.encode("utf-8"))
            Hash = encoder.hexdigest()
            hashInt = int(Hash, 16)
            if hashInt < self.target:
                break
            else:
                nonce += 1
        return nonce, Hash
    def Validate(self):
        data = self.PrepareData(self.Block.Nonce)
        encoder = hashlib.sha256()
        encoder.update(data.encode("utf-8"))
        hashInt = int(encoder.hexdigest(), 16)
        if hashInt < self.target:
            return True
        else:
            return False


        