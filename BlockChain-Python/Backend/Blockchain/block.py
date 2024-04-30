import time
from Backend.Util.crypto_hash import get_crypto_hash
from Backend.Util.hex_to_binary import hex_to_binary
from Backend.config import MINE_RATE

GENESIS_DATA = {
    'timestamp':1,
    'last_hash':'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

class Block:
    """
    _summary_
    Block: unit of storage
    Store transaction in blockchain that support a cryptocurrency.
    """
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
    
    def __repr__(self):
        return (
            'Block: ('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce})'
        )

    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on given last block and data, until a block hash is found that meets the leading 0's proof of work requirements.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = Block.adjust_difficulty(last_block, timestamp) # last_block.difficulty
        nonce = 0
        hash = get_crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            hash = get_crypto_hash(timestamp, last_hash, data, difficulty, nonce)


        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod
    def genesis():
        """
        Generate the genesis block
        """
        # return (
        #     'Block: ('
        #     'timestamp = GENESIS_DATA['timestamp'], 
        #     'last_hash = GENESIS_DATA['last_hash'], 
        #     'hash = GENESIS_DATA['hash'], 
        #     'data = GENESIS_DATA['data'], 
        #     'difficulty = GENESIS_DATA['difficulty'], 
        #     'nonce = GENESIS_DATA['nonce'], 
        # )
        # ? Above Code is written below with destructuring.
        return Block(**GENESIS_DATA)
    
    @staticmethod
    def adjust_difficulty(last_block, new_timestamp):
        """
        Calculate and Adjust difficulty according to MINE_RATE.
        Increase the difficulty for quickly mined blocks.
        Decrease the difficulty for slowly mined blocks.
        """
        if (new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1
        elif (last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1
        else:
            return 1
        
def main():
    genesis_block = Block.genesis()
    block1 = Block.mine_block(genesis_block, 'Jyotil')
    block2 = Block.mine_block(genesis_block, 'Raval')
    print(block1)
    print(block2)
    
if __name__ == '__main__':
    main()