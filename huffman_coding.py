from itertools import count
import heapq
import sys

counter = count()


class Node:
    def __init__(self, key=None, value=None, left=None, right=None):
        self.key = key 
        self.value = value
        self.left_node = left
        self.right_node = right

    def update_node(self, left, right):
        if isinstance(left[2], str):
            left_node = Node(key=left[2], value=left[0])
            self.left_node = left_node
        else:
            self.left_node = left[2]

        if isinstance(right[2], str):
            right_node = Node(key=right[2], value=right[0])
            self.right_node = right_node
        else:
            self.right_node = right[2]

        self.value = left[0] + right[0]
        

def huffman_encoding(data):
    if data is "":
        return data
    
    priority_freq = create_queue(data)

    if len(priority_freq) is 1:
        root = Node()
        root.update_node(heapq.heappop(priority_freq), (0, next(counter), None))
        heapq.heappush(priority_freq, (root.value, next(counter), root))

    while len(priority_freq) != 1:
        root = Node()
        root.update_node(heapq.heappop(priority_freq), heapq.heappop(priority_freq))
        heapq.heappush(priority_freq, (root.value, next(counter), root))

    huffman_tree = heapq.heappop(priority_freq)[2]
    huffman_code = {}
    traverse(huffman_tree, huffman_code, "")
    encoded = encode_data(data, huffman_code)

    return encoded, huffman_tree


def huffman_decoding(data, tree):
    if data is "":
        return data
    
    huffman_code = {}
    reverse_traverse(tree, huffman_code, "")
    decoded_msg = ""
    temp = ""

    while data:
        temp += data[:1]
        data = data[1:]
        
        try:
            decoded_msg += huffman_code[temp]
            temp = ""
        except:
            pass

    return decoded_msg


def reverse_traverse(tree, huffman_code, message):
    if tree.left_node is not None:
        reverse_traverse(tree.left_node, huffman_code, message+"0")
    if tree.right_node is not None:
        reverse_traverse(tree.right_node, huffman_code, message+"1")
    if isinstance(tree.key, str):
        huffman_code[message] = tree.key


def encode_data(data, huffman_code):
    encoded = ""
    
    for char in data:
        encoded += huffman_code[char]

    return encoded
        

def traverse(tree, huffman_code, message):
    if tree.left_node is not None:
        traverse(tree.left_node, huffman_code, message+"0")
    if tree.right_node is not None:
        traverse(tree.right_node, huffman_code, message+"1")
    if isinstance(tree.key, str):
        huffman_code[tree.key] = message


def create_queue(data):
    char_freq = {}
    priority_queue = []
    heapq.heapify(priority_queue)

    for char in data:
        try:
            char_freq[char] += 1
        except:
            char_freq[char] = 1

    for key in char_freq:
        heapq.heappush(priority_queue, (char_freq[key], next(counter), key))

    return priority_queue

       
def simple_node_test():
    root = Node()

    l_node = Node()
    l_node.update_node((5, 1, 'c'), (2, 2, 'd'))
    root.update_node((7, 4, l_node), (1, 3, 'f'))

##    print(root.value)
##    print("Finished testing")



if __name__ == "__main__":
    # Test case 1: regular sentence
    # Test case 2: single character sentence
    sentences = ["The bird is the word", "aaaaa"]

    for a_great_sentence in sentences:
##        print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
##        print("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = huffman_encoding(a_great_sentence)

##        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
##        print("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)
        assert decoded_data == a_great_sentence

##        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
##        print("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 3: empty sentence
    assert huffman_encoding("") == ""
    assert huffman_decoding("", None) == ""

##    print("finished testing")
    
