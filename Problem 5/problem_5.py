# %% [markdown]
# # Building a Trie in Python
# 
# Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
# 
# Before we move into the autocomplete function we need to create a working trie for storing strings.  We will create two classes:
# * A `Trie` class that contains the root node (empty string)
# * A `TrieNode` class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
# 
# Give it a try by implementing the `TrieNode` and `Trie` classes below!

# %%
## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
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
        ## Find the Trie node that represents this prefix
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node

# %% [markdown]
# # Finding Suffixes
# 
# Now that we have a functioning Trie, we need to add the ability to list suffixes to implement our autocomplete feature.  To do that, we need to implement a new function on the `TrieNode` object that will return all complete word suffixes that exist below it in the trie.  For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from `node.suffixes()`.
# 
# Using the code you wrote for the `TrieNode` above, try to add the suffixes function below. (Hint: recurse down the trie, collecting suffixes as you go.)

# %%
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        suffixes = []
        
        for char in self.children:
            temp_char = suffix + char
            char_suffixes = self.children[char].suffixes(temp_char)
            if len(char_suffixes) > 0:
                for char_suffix in char_suffixes:
                    suffixes.append(char_suffix)
            if self.children[char].is_word:
                suffixes.append(temp_char)
                
        return suffixes
            

# %% [markdown]
# # Testing it all out
# 
# Run the following code to add some words to your trie and then use the interactive search box to see what your code returns.

# %%
def test(trie,prefix):
    prefixNode = trie.find(prefix)
    if prefixNode:
        suffixes = prefixNode.suffixes()
        if len(suffixes) > 0:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print("No suffix found")
    else:
        print(prefix + " not found")

# %%
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

#Case 1 
print("\nTest Case 1: Find valid prefix with 1 character") # [nthology , ntagonist , ntonym , nt]
test(MyTrie,"a")

#Case 2
print("\nTest Case 2: Find invalid prefix ") # sa not found
test(MyTrie,"sa")

#Case 2
print("\nTest Case 3: Find valid complete word") # No suffix found
test(MyTrie,"tripod")



# %%



