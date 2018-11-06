#encoding:utf-8
import hashlib
import block as b 
import blockchain as bc
import proofofwork as pfw
import click

#addblock
#printchain
blockchain = bc.Blockchain()
blockchain.NewBlockchain()

@click.group()
def main():
    pass
    

@main.command()
@click.option('--data', help='data of new block')
def addblock(data):
    #print("addblock data: ", data)
    blockchain.AddBlock(data)
    print("Succefully add block")

@main.command()
def printchain():
    print("printchain")

    for item in blockchain:
        print(item)

main.add_command(printchain)
main.add_command(addblock)

if __name__ == '__main__':
    main()

