# coding:utf-8

'''
leetcode 208
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true

说明:
你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

'''

class TrieNode():
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = {}
        self.val = val

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        if word[0] in self.nodes:
            node = self.nodes.get(word[0])
        else:
            self.nodes[word[0]] = 
        
        for char in word:
            if char in cur.nodes:
                cur.nodes[char] = 
        cur.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        

obj = Trie()
obj.insert("abc")
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)