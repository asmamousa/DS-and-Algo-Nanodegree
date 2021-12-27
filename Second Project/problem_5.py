import hashlib
from time import gmtime
import time
import datetime

class Block:

    def __init__(self, GMTtime, data, previous_hash=0):
      self.gmt_time = GMTtime
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next_block = None

    def calc_hash(self):

      try:
        self.check_data()
      except Exception as e:
        raise e

      sha = hashlib.sha256()
      time_str = self.gmt_time.strftime("%a, %d %b %Y %I:%M:%S %p %Z")
      hash_str = (self.data +' '+ time_str).encode('utf-8')
      sha.update(hash_str)
      return sha.hexdigest()

    def check_data(self):
      if self.data == None or len(self.data) == 0:
        raise Exception("The block has invalid data")



class BlockChain:

  def __init__(self):
    self.head = None
    self.tail = None
    self.times = []

  def insert_block(self, block):
    if self.head == None:
      self.head = self.tail = block 
      block.previous_hash = 0
      self.times.append(block.gmt_time)

    else:
      if block.gmt_time in self.times:
        raise Exception("Can't add two blocks which have the same time")

      else:
        block.previous_hash = self.tail.hash
        self.tail.next_block = block
        self.tail = block
        self.times.append(block.gmt_time)

  def print_block_chain(self):
    temp = self.head
    while temp != None:
      print (temp.data)
      temp = temp.next_block


# test case 1: add blocks to the block chain
block_chain = BlockChain()
current_time = datetime.datetime.now(datetime.timezone.utc)
b0 = Block(current_time, 'this is block 0')
block_chain.insert_block(b0)

current_time = datetime.datetime.now(datetime.timezone.utc)
b1 = Block(current_time, 'this is block 1')
block_chain.insert_block(b1)

current_time = datetime.datetime.now(datetime.timezone.utc)
b2 = Block(current_time, 'this is block 2')
block_chain.insert_block(b2)
block_chain.print_block_chain()
# returns 
# this is block 0
# this is block 1
# this is block 2



# test case 2: empty data or Null-value 
block_chain2 = BlockChain()
current_time = datetime.datetime.now(datetime.timezone.utc)
b0 = Block(current_time, '')
block_chain2.insert_block(b0)
# raise an exception with this message Exception: The block has invalid data

current_time = datetime.datetime.now(datetime.timezone.utc)
b1 = Block(current_time, None)
block_chain2.insert_block(b1)
# raise an exception with this message Exception: The block has invalid data

# test case 3: add two blocks with which both have the same time
block_chain3 = BlockChain()
current_time = datetime.datetime.now(datetime.timezone.utc)
b0 = Block(current_time, 'block 0 data')
block_chain3.insert_block(b0)
b1 = Block(current_time, 'block 1 data')
block_chain3.insert_block(b1)
# raise an exception with this message Exception: Can't add two blocks which have the same time

