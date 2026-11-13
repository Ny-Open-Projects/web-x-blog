# 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145248170
import sys  # 提高递归深度上限（深输入防 RecursionError）

sys.setrecursionlimit(200000)  # 树/链表类题目节点数可达 1e4 量级


class TrieNode:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.children = {}  # 把 {} 写入 self.children
        self.is_end = False  # 把 False 写入 self.is_end


class Trie:  # 定义类
    def __init__(self):  # 构造函数：初始化成员
        self.root = TrieNode()  # 把 TrieNode() 写入 根节点

    def insert(self, word):  # 定义函数 insert（参数：self, 单词）
        node = self.root  # 把 self.根节点 存入 节点
        for ch in word:  # 逐个取出 单词 的元素（字符）
            if ch not in node.children:  # 若 字符 not in 节点.children
                node.children[ch] = TrieNode()  # 把 TrieNode() 写入 node.children[ch]
            node = node.children[ch]  # 把 节点.children[字符] 存入 节点
        node.is_end = True  # 把 True 写入 node.is_end

    def search(self, word):  # 定义函数 search（参数：self, 单词）
        node = self._search_prefix(word)  # 把 self._search_prefix(单词) 存入 节点
        return node is not None and node.is_end  # 返回 节点 is not None and 节点.is_end

    def startsWith(self, prefix):  # 定义函数 startsWith（参数：self, prefix）
        return self._search_prefix(prefix) is not None  # 返回 self._search_prefix(prefix) is not None

    def _search_prefix(self, prefix):  # 定义函数 _search_prefix（参数：self, prefix）
        node = self.root  # 把 self.根节点 存入 节点
        for ch in prefix:  # 逐个取出 prefix 的元素（字符）
            if ch not in node.children:  # 若 字符 not in 节点.children
                return None  # 返回 None
            node = node.children[ch]  # 把 节点.children[字符] 存入 节点
        return node  # 返回 节点


if __name__ == "__main__":  # 若 __name__ 等于 '__main__'
    trie = Trie()  # 把 Trie() 存入 trie
    trie.insert("apple")  # trie 插入 「apple」)
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # False
    print(trie.startsWith("app"))  # True
    trie.insert("app")  # trie 插入 「app」)
    print(trie.search("app"))  # True
