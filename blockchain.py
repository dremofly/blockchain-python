#encoding:utf-8
import block as b 
import pickledb

dbFile = 'blocks.db'

class Blockchain(object):
    def __init__(self):
        #self.blocks = []
        self.db = pickledb.load(dbFile, False)
        self.tip = ''
        self.currentHash = ''
    
    def NewBlockchain(self):
        #self.blocks.append(b.Block("GenesisBlock", ''))
        temp = self.db.get('l')
        print('tip: ', temp)
        if temp:
            self.tip = temp
            self.currentHash = temp
        else:
            block = b.Block("GenesisBlock", '')
            self.db.set(block.Hash, block.Serialize())
            self.db.set('l', block.Hash)
            self.tip = block.Hash
            self.currentHash = self.tip
    
    def AddBlock(self, data):
        """
        prevBlockHash = self.blocks[len(self.blocks)-1].Hash 
        newBlock = b.Block(data, prevBlockHash)
        if newBlock.Validate:
            self.blocks.append(newBlock)
            return False
        else:
            return True
        """
        prevBlockHash = self.db.get('l')
        newBlock = b.Block(data, prevBlockHash)
        """
        if newBlock.Validate:
            self.db.put(newBlock.Hash, newBlock)
            self.db.put('l', newBlock.Hash)
            return False
        else:
            return True
            """
        self.db.set(newBlock.Hash, newBlock.Serialize())
        self.db.set('l', newBlock.Hash)
        self.tip = newBlock.Hash
        self.currentHash = newBlock.Hash
        self.db.dump()
        return False
    def __iter__(self):
        return self
    def __next__(self):
        if self.currentHash == '':
            raise StopIteration
            
        block = b.Block()
        block.Deserialize(self.db.get(self.currentHash))
        #print(self.currentHash)
        #print(block)
        self.currentHash = block.PrevBlockHash
        return block
