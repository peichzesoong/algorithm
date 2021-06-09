class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self._root = TrieNode()

    def toIndex(self, ch):
        # Map chars to integer index
        return ord(ch) - ord('a')

    def insert(self, key):
        # Insert key into trie
        # Start at root of trie
        current_node = self._root

        # Traverse characters and add nodes that arent inside
        for char in key.lower():
            index = self.toIndex(char)
            if not current_node.children[index]:
                current_node.children[index] = TrieNode()
            current_node = current_node.children[index]

        # Flip the end flag for leaf of key
        current_node.isEnd = True

    def search(self, key):
        # Search for key in trie
        # Start at the root of the tree
        current_node = self._root

        # Traverse characters
        for char in key.lower():
            index = self.toIndex(char)
            # If node doesnt exist, string cannot be in trie
            if not current_node.children[index]:
                return False
            current_node = current_node.children[index]

        # Check if current node is has end flag and exists
        return current_node != None and current_node.isEnd

    def search_print(self, key):
        print(f'{key} is {"" if self.search(key) else "not "}in trie')