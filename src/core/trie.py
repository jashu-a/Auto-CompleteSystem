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
        suggestions = list()
        prefix_node = self._find_node(prefix)

        if not prefix_node:
            return []
        
        # Helper Funciton for DFS Traversal
        def _collect_words(node: TrieNode, current_word: str):
            if len(suggestions)>=max_suggestions:
                return
            
            if node.is_end_of_word:
                suggestions.append(current_word)

            #Going initially in Sorted Order for predictability and Testing
            for char in sorted(node.children.keys()):
                _collect_words(node.children[char], current_word+char)
            
        _collect_words(prefix_node, prefix)
        return suggestions
    

# For Testing
if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "apricot", "banana", "band", "apply", "application", "aptitude"]
    for word in words:
        trie.insert(word)
            
    print("\nSearching for words:")
    print(f"  'apple' exists: {trie.search('apple')}")      # True
    print(f"  'app' exists: {trie.search('app')}")          # True
    print(f"  'apples' exists: {trie.search('apples')}")    # False
    print(f"  'banana' exists: {trie.search('banana')}")    # True
    print(f"  'bandana' exists: {trie.search('bandana')}")  # False

    print("\nChecking prefixes:")
    print(f"  Starts with 'ap': {trie.starts_with('ap')}")      # True
    print(f"  Starts with 'appl': {trie.starts_with('appl')}")  # True
    print(f"  Starts with 'ban': {trie.starts_with('ban')}")    # True
    print(f"  Starts with 'bat': {trie.starts_with('bat')}")    # False

    print("\nGetting suggestions for prefixes:")
    print(f"  Suggestions for 'ap': {trie.get_suggestions('ap')}")
    # Expected: ['app', 'apple', 'application', 'apply', 'aptitude', 'apricot'] (order might vary based on traversal)
    print(f"  Suggestions for 'appl': {trie.get_suggestions('appl')}")
    # Expected: ['apple', 'application', 'apply']
    print(f"  Suggestions for 'ban': {trie.get_suggestions('ban')}")
    # Expected: ['banana', 'band']
    print(f"  Suggestions for 'z': {trie.get_suggestions('z')}")
    # Expected: []

    print("\nGetting suggestions with limit:")
    print(f"  Suggestions for 'ap' (max 3): {trie.get_suggestions('ap', max_suggestions=3)}")
    # Expected: 3 suggestions
    print(f"  Suggestions for 'a' (max 2): {trie.get_suggestions('a', max_suggestions=2)}")
    # Expected: 2 suggestions (could be 'app', 'apple' or similar)