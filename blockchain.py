#encoding:utf-8
import block as b 

class Blockchain(object):
    def __init__(self):
        self.blocks = []
    
    def NewBlockchain(self):
        self.blocks.append(b.Block("GenesisBlock", ''))
    
    def AddBlock(self, data):
        prevBlockHash = self.blocks[len(self.blocks)-1].Hash 
        newBlock = b.Block(data, prevBlockHash)
        self.blocks.append(newBlock)
