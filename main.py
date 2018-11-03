#encoding:utf-8
import hashlib
import block as b 
import blockchain as bc

blockchain = bc.Blockchain()
blockchain.NewBlockchain()
blockchain.AddBlock("Send 1 BTC to Hong")
blockchain.AddBlock("Send 2 BTC to Hong")

for block in blockchain.blocks:
    print("Prevhash: ", block.PrevBlockHash)
    print("Data: ", block.Data)
    print("Hash: ", block.Hash)
    print("\n")