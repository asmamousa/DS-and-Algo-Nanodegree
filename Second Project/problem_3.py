import sys
from heapq import heapify, heappush, heappop
from functools import total_ordering

@total_ordering
class Node():
    def __init__(self, char, frequency):
        self.char = char
        self.freq = frequency
        self.left = None
        self.right = None
        self.left_link = None
        self.right_link = None

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.freq == other.freq

    def __lt__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.freq < other.freq

class Helper():
    def build_freq_table(self, data):
        freq_table = dict()
        # find occurance of each char in the string
        for char in data:
            if char not in freq_table:
                freq_table[char] = data.count(char)

        return freq_table


    def build_heap(self, freq_table):
        local_heap = []
        heapify(local_heap)
     
        # Adding items to the min-heap
        for key in freq_table:
            node = Node(key,freq_table[key])
            heappush(local_heap, node)

        return local_heap


    def build_huffman_tree(self, heap):

        while len(heap) > 1:
            # 1. extract two min values
            left_child = heappop(heap)
            right_child = heappop(heap)

            # 2. create an internal node in tree which has sum of two frequencies and assign values for each link
            internal_node = Node(None, left_child.freq + right_child.freq)
            internal_node.left = left_child
            internal_node.left_link = 0
            internal_node.right = right_child
            internal_node.right_link = 1

            heappush(heap, internal_node)
        return heap


    def extract_code(self, code_list):
        code_string = ''

        for i in code_list:
            code_string = code_string + str(i)

        return code_string


    def generate_huffman_code(self, node, code=[], huffman_code_dict={}):

        if node.right == None and node.left == None:
            code_str = self.extract_code(code)
            huffman_code_dict[node.char] = code_str
            code.pop()
            return

        code.append(node.left_link)
        self.generate_huffman_code(node.left, code, huffman_code_dict)

        code.append(node.right_link)
        self.generate_huffman_code(node.right, code, huffman_code_dict)

        if len(code) > 0:
            code.pop()
        return huffman_code_dict

    def encode(self, data, huffman_code):
        encoded_data = ''

        for char in data:
            encoded_data+= huffman_code[char]

        return encoded_data


class Huffman_Coding():
    def __init__(self):
        self.helper = Helper()


    def huffman_encoding(self, data):

        if data == None or data == '':
            return None, None

        # 1. build frequency table
        freq_table = self.helper.build_freq_table(data)
        
        # 2. add all in freq dict to min-heap
        heap = self.helper.build_heap(freq_table)

        # 3. build Huffman tree
        huffman_tree = self.helper.build_huffman_tree(heap)
        
        # 4. generate code for each char in data(string)
        code_dict = self.helper.generate_huffman_code(huffman_tree[0])

        # 5. return the whole encoded data
        encoded_data = self.helper.encode(data, code_dict)

        return encoded_data, huffman_tree


    def huffman_decoding(self, data, tree):

        if data == None or data == '':
            return

        if tree is None or len(tree) == 0:
            return

        decoded_string = ''
        curr_node = tree[0]
        for c in data+' ':
            if curr_node.right == None and curr_node.left == None:
                decoded_string = decoded_string + (curr_node.char)
                curr_node = tree[0]

            if c == ' ':
                break

            if int(c) == 0:
                curr_node = curr_node.left
            elif int(c) == 1:
                curr_node = curr_node.right

        return decoded_string
        



huffman_coding = Huffman_Coding()
# test case 1:
string_input_list = ['AAAAAAABBBCCCCCCCDDEEEEEE', 'The bird is the word']


for string_input in string_input_list:

    print ("The size of the data is: {}\n".format(sys.getsizeof(string_input)))
    print ("The content of the data is: {}\n".format(string_input))

    encoded_data, tree = huffman_coding.huffman_encoding(string_input)

    if encoded_data and tree:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_coding.huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

# expected output is this:
# 1. for AAAAAAABBBCCCCCCCDDEEEEEE:
# The size of the data is: 74
# The content of the data is: AAAAAAABBBCCCCCCCDDEEEEEE
# The size of the encoded data is: 32
# The content of the encoded data is: 1010101010101000100100111111111111111000000010101010101
# The size of the decoded data is: 74
# The content of the encoded data is: AAAAAAABBBCCCCCCCDDEEEEEE

# 2. for The bird is the word:
# The size of the data is: 69
# The content of the data is: The bird is the word
# The size of the encoded data is: 36
# The content of the encoded data is: 1000111111100100001101110000101110110110100011111111001101010011100001
# The size of the decoded data is: 69
# The content of the encoded data is: The bird is the word

# test case 2, 3: empty string and None value
string_input_list= ['', None]
for string_input in string_input_list:
    print ("The size of the data is: {}\n".format(sys.getsizeof(string_input)))
    print ("The content of the data is: {}\n".format(string_input))

    encoded_data, tree = huffman_coding.huffman_encoding(string_input)

    if encoded_data and tree:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_coding.huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

# for '' -> empty string
# The size of the data is: 49
# The content of the data is: 

# for None:
# The size of the data is: 16
# The content of the data is: None




