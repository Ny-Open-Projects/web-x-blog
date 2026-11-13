// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145248170
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type TrieNode struct { // 定义类型
	children map[rune]*TrieNode // children 映射表[rune] 乘 TrieNode
	isEnd    bool               // isEnd bool
}

type Trie struct { // 定义类型
	root *TrieNode // 根节点 乘 TrieNode
}

func NewTrie() *Trie { // 定义函数/方法 NewTrie
	return &Trie{root: &TrieNode{children: map[rune]*TrieNode{}}}
}

func (t *Trie) insert(word string) { // 定义函数/方法 insert
	node := t.root            // 把 另一字符串.根节点 写入 node :
	for _, ch := range word { // 同时取 _ 与 字符 遍历
		key := ch                             // 把 字符 写入 key :
		if _, ok := node.children[key]; !ok { // 若 _, ok : 赋值为 节点.children[key]; 取反 ok
			node.children[key] = &TrieNode{children: map[rune]*TrieNode{}}
		}
		node = node.children[key] // 把 节点.children[key] 写入 节点
	}
	node.isEnd = true // 把 true 写入 node.isEnd
}

func (t *Trie) searchPrefix(prefix string) *TrieNode { // 定义函数/方法 searchPrefix
	node := t.root              // 把 另一字符串.根节点 写入 node :
	for _, ch := range prefix { // 同时取 _ 与 字符 遍历
		n, ok := node.children[ch] // 把 节点.children[字符] 写入 n, ok :
		if !ok {                   // 若 取反 ok
			return nil // 返回 nil
		}
		node = n // 把 元素个数 写入 节点
	}
	return node // 返回 节点
}

func (t *Trie) search(word string) bool { // 定义函数/方法 search
	node := t.searchPrefix(word)     // 把 另一字符串.searchPrefix(单词) 写入 node :
	return node != nil && node.isEnd // 返回 节点 不等于 nil 且 节点.isEnd
}

func (t *Trie) startsWith(prefix string) bool { // 定义函数/方法 startsWith
	return t.searchPrefix(prefix) != nil // 返回 另一字符串.searchPrefix(prefix) 不等于 nil
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                 // 把 true 写入 ok :
	trie := NewTrie()          // 把 NewTrie() 写入 trie :
	trie.insert("apple")       // trie 插入 「apple」)
	if !trie.search("apple") { // 若 取反 trie.search(「apple」
		ok = false                       // 把 false 写入 ok
		fmt.Println("FAIL search apple") // 打印输出
	}
	if trie.search("app") { // 若 trie.search(「app」
		ok = false                     // 把 false 写入 ok
		fmt.Println("FAIL search app") // 打印输出
	}
	if !trie.startsWith("app") { // 若 取反 trie.startsWith(「app」
		ok = false                         // 把 false 写入 ok
		fmt.Println("FAIL startsWith app") // 打印输出
	}
	trie.insert("app")       // trie 插入 「app」)
	if !trie.search("app") { // 若 取反 trie.search(「app」
		ok = false                      // 把 false 写入 ok
		fmt.Println("FAIL search app2") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
