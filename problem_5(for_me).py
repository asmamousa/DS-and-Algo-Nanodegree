import collections

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
    
    def insert(self, char):
        self.children[char] = TrieNode()

    def find_suffixes(self, suffix, suff_list):

        if self.is_word:
            suff_list.append(suffix)
            if not self.children:
                suffix = ''

        for k in self.children:
            suffix += k
            self.children[k].find_suffixes(suffix, suff_list)
            # after each child, I removed the last char which is the sibling for the current char
            # because we finshed the sibling's path until the end
            # and now we are in traversing in the current char path
            suffix = suffix[0:-1]
            

    def suffixes(self, suffix = ''):

        suff_list = [] 
        self.find_suffixes(suffix, suff_list)
        return suff_list

        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node

    def exists(self, prefix):
        current_node = self.root

        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word

MyTrie = Trie()
wordList = ["fun", "function", "factory", "funtazia"]
for word in wordList:
    MyTrie.insert(word)

for word in wordList:
    if MyTrie.exists(word):
            print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")


f(prefix='f')

