from Backend.Blockchain.block import Block

class BlockChain:
    """
    _summary_
    Blockchain class
    Implemented as list of block and data sets for transactions.
    """
    def __init__(self):
        self.chain = [Block.genesis()]
        
    def __repr__(self):
        return f"BlockChain: {self.chain}"
        
    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))
        
        
def main():
    blockchain_instance = BlockChain()
    blockchain_instance.add_block(False)
    blockchain_instance.add_block('One')
    blockchain_instance.add_block('Two')
    blockchain_instance.add_block('Three')
    blockchain_instance.add_block(4)
    blockchain_instance.add_block([5])
    blockchain_instance.add_block([6.0])
    blockchain_instance.add_block(7.0001)

    print(blockchain_instance)
    
if __name__ == '__main__':
    main()