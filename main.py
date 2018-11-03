#encoding:utf-8
import hashlib
import block as b 
import blockchain as bc
import proofofwork as pfw

blockchain = bc.Blockchain()
blockchain.NewBlockchain()
err = blockchain.AddBlock("Send 1 BTC to Hong")
if err:
    print("[Warning!] Failed to add block \"%s\""%("Send 1 BTC to Hong"))
blockchain.AddBlock("Send 2 BTC to Hong")
if err:
    print("[Warning!] Failed to add block \"%s\""%("Send 2 BTC to Hong"))

for block in blockchain.blocks:
    print(block)