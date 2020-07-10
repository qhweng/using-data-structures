from itertools import count
import datetime
import hashlib

counter = count()


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        sha.update(str(self.index).encode('utf-8'))
        sha.update(str(self.timestamp).encode('utf-8'))
        sha.update(self.data.encode('utf-8'))
        sha.update(str(self.previous_hash).encode('utf-8'))

        return sha.hexdigest()


class Blockchain:
    def __init__(self):
        self.head_block = None
        self.curr_block = None

    def append_block(self, data):
        if data is None or data is "":
            return
        
        time = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M %-m/%-d/%Y")
        
        if self.head_block is None:
            block = Block(next(counter), time, data, 0)
            self.head_block = block
            self.curr_block = block
        else:
            block = Block(next(counter), time, data, self.curr_block)
            self.curr_block = block

    def hash_list(self):
        if self.head_block is None:
            return []
        
        list_blocks = []
        block = self.curr_block

        for i in range(0, self.curr_block.index + 1):
            list_blocks = [block] + list_blocks
            block = block.previous_hash

        return list_blocks


def test():
    blockchain = Blockchain()

    for i in range(5):
        data = "DATA BLOCK " + str(i)
        blockchain.append_block(data)

##    print("Finished building blocks...\n")

    # Test normal cases
    hash_list = blockchain.hash_list()
    assert hash_list[0].data == "DATA BLOCK 0"
    assert hash_list[2].data == "DATA BLOCK 2"
    assert len(hash_list) == 5

    # Test empty block
    blockchain.append_block("")
    hash_list = blockchain.hash_list()
    assert len(hash_list) == 5

    # Test empty blockchain with empty block
    empty_blockchain = Blockchain()
    hash_list = empty_blockchain.hash_list()
    assert len(hash_list) == 0
    blockchain.append_block("")
    assert empty_blockchain.head_block is None
    assert empty_blockchain.curr_block is None
    assert len(hash_list) == 0

##    print("Finished Test Case 1")

test()
