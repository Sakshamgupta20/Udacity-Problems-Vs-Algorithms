Here we are using trie data structure to find suffixes
We store Words in form on Trie with help of TrieNode

To get suffixes i am using Recurssion of nested children nodes and then appending it to final list.

Suffixes method takes a empty string input by default as we go deep inside Trie we keep appending child to that suffix and then return it as soon as we reach at bottom of Trie

We use backtracking to find all suffixes.

Time Complexity - O(N) As it will parse complete list to get suffixes
Space Complexity - O(N) Temporary list used to store suffixes 

Worst Case - When all words are same but last characters are different e.g. ["problem","problems","problemss"]
