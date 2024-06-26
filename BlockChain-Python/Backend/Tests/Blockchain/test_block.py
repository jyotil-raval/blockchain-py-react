import time
from Backend.Blockchain.block import Block, GENESIS_DATA
from Backend.config import MINE_RATE, SECONDS
from Backend.Util.hex_to_binary import hex_to_binary

def test_mine_block():
    first_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(first_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == first_block.hash
    assert hex_to_binary(block.hash)[0:block.difficulty] == '0' * block.difficulty

def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, value in GENESIS_DATA.items():
        getattr(genesis, key) == value

def test_quickly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'foo')
    mined_block = Block.mine_block(last_block, 'bar')

    assert mined_block.difficulty == last_block.difficulty + 1

def test_slowly_mined_block():
    last_block = Block.mine_block(Block.genesis(), 'foo')
    time.sleep(MINE_RATE/SECONDS)
    mined_block = Block.mine_block(last_block, 'bar')
    assert mined_block.difficulty == last_block.difficulty - 1

def test_mined_block_difficulty_limits_at_1():
    last_block = Block(
        time.time_ns(),
        'test_last_block_hash',
        'test_block_hash',
        'test_block_data',
        1,
        0
    )
    time.sleep(MINE_RATE/SECONDS)
    mined_block = Block.mine_block(last_block, 'bar')
    assert mined_block.difficulty == 1