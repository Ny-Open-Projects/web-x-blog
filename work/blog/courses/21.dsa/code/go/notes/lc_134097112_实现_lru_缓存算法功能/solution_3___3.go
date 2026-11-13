// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type lruNode struct { // 定义类型
	key   int      // key int
	value int      // value int
	prev  *lruNode // 前一个 乘 lruNode
	next  *lruNode // 下一个 乘 lruNode
}

type LRUCache struct { // 定义类型
	length int              // 长度 int
	data   map[int]*lruNode // data 映射表[int] 乘 lruNode
	head   *lruNode         // 头节点 乘 lruNode
	tail   *lruNode         // 尾节点 乘 lruNode
}

func NewLRU(length int) *LRUCache { // 定义函数/方法 NewLRU
	head := &lruNode{} // 把 按位与 lruNode{} 写入 head :
	tail := &lruNode{} // 把 按位与 lruNode{} 写入 tail :
	head.next = tail   // 把 尾节点 写入 下一个
	tail.prev = head   // 把 头节点 写入 前一个
	return &LRUCache{length: length, data: make(map[int]*lruNode), head: head, tail: tail}
}

func (c *LRUCache) removeNode(n *lruNode) { // 定义函数/方法 removeNode
	n.prev.next = n.next // 把 元素个数.下一个 写入 下一个
	n.next.prev = n.prev // 把 元素个数.前一个 写入 前一个
}

func (c *LRUCache) addToTail(n *lruNode) { // 定义函数/方法 addToTail
	n.prev = c.tail.prev // 把 字符.尾节点.前一个 写入 前一个
	n.next = c.tail      // 把 字符.尾节点 写入 下一个
	c.tail.prev.next = n // 把 元素个数 写入 下一个
	c.tail.prev = n      // 把 元素个数 写入 前一个
}

func (c *LRUCache) set(key, value int) { // 定义函数/方法 set
	if n, ok := c.data[key]; ok { // 若 元素个数, ok : 赋值为 字符.data[key]; ok
		c.removeNode(n) // 字符.removeNode(元素个数)
	}
	n := &lruNode{key: key, value: value} // 把 按位与 lruNode{key: key, value: value} 写入 n :
	c.data[key] = n                       // 把 元素个数 写入 c.data[key]
	c.addToTail(n)                        // 字符.addToTail(元素个数)
	if len(c.data) > c.length {           // 若 长度(字符.data) 超过 字符.长度
		lru := c.head.next      // 把 字符.头节点.下一个 写入 lru :
		c.removeNode(lru)       // 字符.removeNode(lru)
		delete(c.data, lru.key) // delete(字符.data, lru.key)
	}
}

func (c *LRUCache) get(key int) (int, bool) { // 定义函数/方法 get
	n, ok := c.data[key] // 把 字符.data[key] 写入 n, ok :
	if !ok {             // 若 取反 ok
		return 0, false // 返回 0, false
	}
	c.removeNode(n)      // 字符.removeNode(元素个数)
	c.addToTail(n)       // 字符.addToTail(元素个数)
	return n.value, true // 返回 元素个数.value, true
}

func main() { // 程序入口：跑内嵌自测用例
	c := NewLRU(2)      // 把 NewLRU(2) 写入 c :
	c.set(1, 1)         // 字符.set(1, 1)
	c.set(2, 2)         // 字符.set(2, 2)
	r1, _ := c.get(1)   // 把 字符 查找 1) 写入 r1, _ :
	c.set(3, 3)         // 字符.set(3, 3)
	_, r2ok := c.get(2) // 把 字符 查找 2) 写入 _, r2ok :
	c.set(4, 4)         // 字符.set(4, 4)
	_, r3ok := c.get(1) // 把 字符 查找 1) 写入 _, r3ok :
	r4, _ := c.get(3)   // 把 字符 查找 3) 写入 r4, _ :
	r5, _ := c.get(4)   // 把 字符 查找 4) 写入 r5, _ :
	ok := true          // 把 true 写入 ok :
	if r1 != 1 {        // 若 r1 不等于 1
		ok = false             // 把 false 写入 ok
		fmt.Println("FAIL r1") // 打印输出
	}
	if r2ok { // 若 r2ok
		ok = false                            // 把 false 写入 ok
		fmt.Println("FAIL r2 should be None") // 打印输出
	}
	if r3ok { // 若 r3ok
		ok = false                            // 把 false 写入 ok
		fmt.Println("FAIL r3 should be None") // 打印输出
	}
	if r4 != 3 { // 若 r4 不等于 3
		ok = false             // 把 false 写入 ok
		fmt.Println("FAIL r4") // 打印输出
	}
	if r5 != 4 { // 若 r5 不等于 4
		ok = false             // 把 false 写入 ok
		fmt.Println("FAIL r5") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
