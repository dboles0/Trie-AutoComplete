# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields 
  
    def __init__(self, isRootNode):
        # The initialization below is just a suggestion.
        # Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mapping each character from a-z to 
                       # the child node if any corresponding to that character.


    def addWord(self,w):
        assert(len(w) > 0)
        
        cur = self
        
        # loop thorught list and add if not found
        for ch in w:
            # check if the character is found in the next node edge
            if ch in cur.next: 
                # itterate to next node
                cur = cur.next[ch]
            else: 
                # create new node
                newNode = MyTrieNode(False)
                # point to cur's next
                cur.next[ch] = newNode
                # reassemble cur to newNode
                cur = newNode
                
        # add end of word flag and count
        cur.isWordEnd = True
        cur.count += 1
        
        return
    
    def lookupWord(self,w):
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.
        
        cur = self
        
        for ch in w: 
            if ch in cur.next:
                cur = cur.next[ch]
            else: 
                return 0
                
        return cur.count
        
    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j
        
        cur = self
        
        # evaluate the prefix returning empty list if there are 
        # no successor nodes
        for ch in w: 
            if ch in cur.next: 
                cur = cur.next[ch]
            else: 
                return []
        # evaluate each successor path to create word and count        
        return self.stringCompletion(cur, w, [])
    
    def stringCompletion(self, root, auto_word, s_j): 
        # if we found the end of word save word and count
        if root.isWordEnd: 
            s_j.append((auto_word, root.count))
        
        # if we have a next node resurse through successors
        if root.next:
            for ch in root.next:
                # catch all paths for s_j
                s_j = self.stringCompletion(root.next[ch], (auto_word + ch), s_j)
        return s_j


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tests for program
        
t= MyTrieNode(True) # Create a root Trie node
lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']
# Insert the words in lst1
for w in lst1:
    t.addWord(w)
    
# Perform lookups
j = t.lookupWord('testy') # should return 0
j2 = t.lookupWord('telltale') # should return 0
j3 = t.lookupWord ('testing') # should return 2

# Run autocompletes
lst3 = t.autoComplete('pi')
print('Completions for \"pi\" are : ')
print(lst3)

lst4 = t.autoComplete('tes')
print('Completions for \"tes\" are : ')
print(lst4)
