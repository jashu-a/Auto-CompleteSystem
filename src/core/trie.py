class TrieNode:
    """
    A node in the Trie Data Structure.
    Each node represents a character in a word.
    """
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """
    A Trie (prefix tree) implementation for efficient word storage and prefix-based search.
    """
    def __init__(self):
        self.root=TrieNode()
    
    def insert(self,word:str):
        """
        Inserts a word into a Trie
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char]=TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word:str) -> bool:
        """
        Checks if a word exists in the Trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix:str) -> bool:
        """
        Checks if any word in the Trie starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def _find_node(self, prefix:str) -> TrieNode | None:
        """
        Helper method to find the node corresponding to the end of a given prefix.
        Returns None if the prefix does not exist in the Trie.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node=node.children[char]
        return node
    
    def get_suggestions(self, prefix:str, max_suggestions: int = 10) -> list[str]:
        """
        Retrieves all words in the Trie that start with the given prefix. 
        Optionally limits the number to 10.
        """
        