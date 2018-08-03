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
        self.childs = [] #当前节点的所有子节点
        self.data = "" #当前节点的表示的字符串
        self.isLeaf = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        i = 0
        while(i<len(word)):
            prefix = cur.data + word[i]

            # 构建当前节点所有子节点的hashmap
            hash_map = {}
            for node in cur.childs:
                hash_map[node.data] = node

            # 判断前缀是否在子节点中
            if prefix in hash_map:
                cur = hash_map[prefix]
            else:
                new_node = TrieNode()
                new_node.data = prefix
                cur.childs.append(new_node)
                cur = new_node
            #当i访问到最后一个字符时，将节点置为叶节点
            if i == len(word)-1:
                cur.isLeaf = True
            i += 1


    def search(self, word):
        cur = self.root
        i = 0
        while i < len(word):
            prefix = cur.data + word[i]
            # 构建当前节点所有子节点的hashmap
            hash_map = {}
            for node in cur.childs:
                hash_map[node.data] = node
            # 判断前缀是否在子节点中
            if prefix in hash_map:
                cur = hash_map[prefix]
            else:
                return False
            i += 1

        if i == len(word) and cur.isLeaf == True:
            return True
        else:
            return False

    def startsWith(self, word):
        # 判断是否有前缀word节点
        cur = self.root
        i = 0
        while i < len(word):
            prefix = cur.data + word[i]
            # 构建当前节点所有子节点的hashmap
            hash_map = {}
            for node in cur.childs:
                hash_map[node.data] = node

            # 判断前缀是否在子节点中
            if prefix in hash_map:
                cur = hash_map[prefix]
            else:
                return False
            i += 1

        if i == len(word):
            return True
        else:
            return False

obj = Trie()
obj.insert("a")
obj.insert("apps")
print(obj.search("apps"))