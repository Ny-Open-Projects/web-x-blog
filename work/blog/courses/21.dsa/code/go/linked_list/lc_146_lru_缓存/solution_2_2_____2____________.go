// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094527
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

type DLinkedNode struct { // 定义类型
	key   int          // key int
	value int          // value int
	prev  *DLinkedNode // 前一个 乘 DLinkedNode
	next  *DLinkedNode // 下一个 乘 DLinkedNode
}

type LRUCache struct { // 定义类型
	size     int                  // 大小 int
	capacity int                  // capacity int
	cache    map[int]*DLinkedNode // cache 映射表[int] 乘 DLinkedNode
	head     *DLinkedNode         // 头节点 乘 DLinkedNode
	tail     *DLinkedNode         // 尾节点 乘 DLinkedNode
}

func Constructor(capacity int) LRUCache { // 定义函数/方法 Constructor
	lru := LRUCache{ // 把 LRUCache{ 写入 lru :
		cache:    make(map[int]*DLinkedNode),
		capacity: capacity,
	}
	lru.head = &DLinkedNode{} // 把 按位与 DLinkedNode{} 写入 头节点
	lru.tail = &DLinkedNode{} // 把 按位与 DLinkedNode{} 写入 尾节点
	lru.head.next = lru.tail  // 把 lru.尾节点 写入 下一个
	lru.tail.prev = lru.head  // 把 lru.头节点 写入 前一个
	return lru                // 返回 lru
}

func (this *LRUCache) Get(key int) int { // 定义函数/方法 Get
	if node, ok := this.cache[key]; ok { // 若 节点, ok : 赋值为 this.cache[key]; ok
		this.moveToHead(node) // this.moveToHead(节点)
		return node.value     // 返回 节点.value
	}
	return -1 // 返回 减 1
}

func (this *LRUCache) Put(key int, value int) { // 定义函数/方法 Put
	if node, ok := this.cache[key]; ok { // 若 节点, ok : 赋值为 this.cache[key]; ok
		node.value = value    // 把 value 写入 node.value
		this.moveToHead(node) // this.moveToHead(节点)
	} else { // 否则
		node := &DLinkedNode{key: key, value: value} // 把 按位与 DLinkedNode{key: key, value: value} 写入 node :
		this.cache[key] = node                       // 把 节点 写入 this.cache[key]
		this.addToHead(node)                         // this.addToHead(节点)
		this.size++                                  // this.大小 加一
		if this.size > this.capacity {               // 若 this.大小 超过 this.capacity
			removed := this.removeTail()    // 把 this.removeTail() 写入 removed :
			delete(this.cache, removed.key) // delete(this.cache, removed.key)
			this.size--                     // this.大小 减一
		}
	}
}

func (this *LRUCache) addToHead(node *DLinkedNode) { // 定义函数/方法 addToHead
	node.prev = this.head      // 把 this.头节点 写入 前一个
	node.next = this.head.next // 把 this.头节点.下一个 写入 下一个
	this.head.next.prev = node // 把 节点 写入 前一个
	this.head.next = node      // 把 节点 写入 下一个
}

func (this *LRUCache) removeNode(node *DLinkedNode) { // 定义函数/方法 removeNode
	node.prev.next = node.next // 把 节点.下一个 写入 下一个
	node.next.prev = node.prev // 把 节点.前一个 写入 前一个
}

func (this *LRUCache) moveToHead(node *DLinkedNode) { // 定义函数/方法 moveToHead
	this.removeNode(node) // this.removeNode(节点)
	this.addToHead(node)  // this.addToHead(节点)
}

func (this *LRUCache) removeTail() *DLinkedNode { // 定义函数/方法 removeTail
	node := this.tail.prev // 把 this.尾节点.前一个 写入 node :
	this.removeNode(node)  // this.removeNode(节点)
	return node            // 返回 节点
}

func main() { // 程序入口：跑内嵌自测用例
	c := Constructor(2)                // 把 Constructor(2) 写入 c :
	c.Put(1, 1)                        // 字符.Put(1, 1)
	c.Put(2, 2)                        // 字符.Put(2, 2)
	g1 := c.Get(1)                     // 把 字符.Get(1) 写入 g1 :
	c.Put(3, 3)                        // 字符.Put(3, 3)
	g2 := c.Get(2)                     // 把 字符.Get(2) 写入 g2 :
	c.Put(4, 4)                        // 字符.Put(4, 4)
	g3 := c.Get(1)                     // 把 字符.Get(1) 写入 g3 :
	g4 := c.Get(3)                     // 把 字符.Get(3) 写入 g4 :
	g5 := c.Get(4)                     // 把 字符.Get(4) 写入 g5 :
	got := []int{g1, g2, g3, g4, g5}   // 把 []int{g1, g2, g3, g4, g5} 写入 got :
	want := []int{1, -1, -1, 3, 4}     // 把 []int{1, 减 1, 减 1, 3, 4} 写入 want :
	if !reflect.DeepEqual(got, want) { // 若 取反 reflect.DeepEqual(got, want
		fmt.Printf("FAIL got=%v want=%v\n", got, want) // 打印输出
		panic("FAILED")                                // panic(「FAILED」)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
