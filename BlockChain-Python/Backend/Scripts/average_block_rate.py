import time
from Backend.Blockchain.blockchain import BlockChain
from Backend.config import SECONDS

blockchain = BlockChain()
times = []

for i in range(1000):
    start_time = time.time_ns()
    blockchain.add_block(i)
    end_time = time.time_ns()

    time_to_maine = (end_time - start_time) / SECONDS
    times.append(time_to_maine)

    average_time = sum(times) / len(times)

    print(f'new Bloc difficulty: {blockchain.chain[-1].difficulty}')
    print(f'time to mine new block: {time_to_maine}s')
    print(f'average time to add block: {average_time}s\n')