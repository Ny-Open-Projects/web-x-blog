// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145346697
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

type lfuNode struct { // 定义类型
	key   int      // key int
	value int      // value int
	freq  int      // 频次表 int
	prev  *lfuNode // 前一个 乘 lfuNode
	next  *lfuNode // 下一个 乘 lfuNode
}

type doublyLinkedList struct { // 定义类型
	head *lfuNode // 头节点 乘 lfuNode
	tail *lfuNode // 尾节点 乘 lfuNode
	size int      // 大小 int
}

func newDLL() *doublyLinkedList { // 定义函数/方法 newDLL
	d := &doublyLinkedList{} // 把 按位与 doublyLinkedList{} 写入 d :
	d.head = &lfuNode{}      // 把 按位与 lfuNode{} 写入 头节点
	d.tail = &lfuNode{}      // 把 按位与 lfuNode{} 写入 尾节点
	d.head.next = d.tail     // 把 d.尾节点 写入 下一个
	d.tail.prev = d.head     // 把 d.头节点 写入 前一个
	d.size = 0               // 把 0 写入 大小
	return d                 // 返回 d
}

func (d *doublyLinkedList) add(node *lfuNode) { // 定义函数/方法 add
	node.prev = d.head      // 把 d.头节点 写入 前一个
	node.next = d.head.next // 把 d.头节点.下一个 写入 下一个
	d.head.next.prev = node // 把 节点 写入 前一个
	d.head.next = node      // 把 节点 写入 下一个
	d.size++                // d.大小 加一
}

func (d *doublyLinkedList) remove(node *lfuNode) { // 定义函数/方法 remove
	node.prev.next = node.next // 把 节点.下一个 写入 下一个
	node.next.prev = node.prev // 把 节点.前一个 写入 前一个
	d.size--                   // d.大小 减一
}

func (d *doublyLinkedList) removeLast() *lfuNode { // 定义函数/方法 removeLast
	if d.size == 0 { // 若 d.大小 等于 0
		return nil // 返回 nil
	}
	node := d.tail.prev // 把 d.尾节点.前一个 写入 node :
	d.remove(node)      // d 弹出 节点)
	return node         // 返回 节点
}

func (d *doublyLinkedList) isEmpty() bool { // 定义判定函数 isEmpty
	return d.size == 0 // 返回 d.大小 等于 0
}

type lfuCache struct { // 定义类型
	capacity   int                       // capacity int
	size       int                       // 大小 int
	keyToNode  map[int]*lfuNode          // keyToNode 映射表[int] 乘 lfuNode
	freqToList map[int]*doublyLinkedList // freqToList 映射表[int] 乘 doublyLinkedList
	minFreq    int                       // minFreq int
}

func newLFU(capacity int) *lfuCache { // 定义函数/方法 newLFU
	return &lfuCache{ // 返回 按位与 lfuCache{
		capacity:   capacity,
		keyToNode:  map[int]*lfuNode{},
		freqToList: map[int]*doublyLinkedList{},
		minFreq:    0,
	}
}

func (c *lfuCache) updateFreq(node *lfuNode) { // 定义函数/方法 updateFreq
	freq := node.freq                 // 把 节点.频次表 写入 freq :
	c.freqToList[freq].remove(node)   // 字符.freqToList[频次表] 弹出 节点)
	if c.freqToList[freq].isEmpty() { // 若 字符.freqToList[频次表].isEmpty(
		delete(c.freqToList, freq) // delete(字符.freqToList, 频次表)
		if c.minFreq == freq {     // 若 字符.minFreq 等于 频次表
			c.minFreq++ // 字符.minFreq 加一
		}
	}
	node.freq++                                // 节点.频次表 加一
	if _, ok := c.freqToList[node.freq]; !ok { // 若 _, ok : 赋值为 字符.freqToList[节点.频次表]; 取反 ok
		c.freqToList[node.freq] = newDLL() // 把 newDLL() 写入 c.freqToList[node.freq]
	}
	c.freqToList[node.freq].add(node) // 字符.freqToList[节点.频次表] 追加 节点)
}

func (c *lfuCache) get(key int) int { // 定义函数/方法 get
	node, ok := c.keyToNode[key] // 把 字符.keyToNode[key] 写入 node, ok :
	if !ok {                     // 若 取反 ok
		return -1 // 返回 减 1
	}
	c.updateFreq(node) // 字符.updateFreq(节点)
	return node.value  // 返回 节点.value
}

func (c *lfuCache) put(key, value int) { // 定义函数/方法 put
	if c.capacity <= 0 { // 若 字符.capacity 不超过 0
		return // return
	}
	if node, ok := c.keyToNode[key]; ok { // 若 节点, ok : 赋值为 字符.keyToNode[key]; ok
		node.value = value // 把 value 写入 node.value
		c.updateFreq(node) // 字符.updateFreq(节点)
		return             // return
	}
	if c.size >= c.capacity { // 若 字符.大小 不低于 字符.capacity
		minList := c.freqToList[c.minFreq] // 把 字符.freqToList[字符.minFreq] 写入 minList :
		removed := minList.removeLast()    // 把 minList.removeLast() 写入 removed :
		if removed != nil {                // 若 removed 不等于 nil
			delete(c.keyToNode, removed.key) // delete(字符.keyToNode, removed.key)
			c.size--                         // 字符.大小 减一
		}
	}
	node := &lfuNode{key: key, value: value, freq: 1} // 把 按位与 lfuNode{key: key, value: value, 频次表: 1} 写入 node :
	c.keyToNode[key] = node                           // 把 节点 写入 c.keyToNode[key]
	if _, ok := c.freqToList[1]; !ok {                // 若 _, ok : 赋值为 字符.freqToList[1]; 取反 ok
		c.freqToList[1] = newDLL() // 把 newDLL() 写入 c.freqToList[1]
	}
	c.freqToList[1].add(node) // 字符.freqToList[1] 追加 节点)
	c.minFreq = 1             // 把 1 写入 c.minFreq
	c.size++                  // 字符.大小 加一
}

func main() { // 程序入口：跑内嵌自测用例
	lfu := newLFU(2)                   // 把 newLFU(2) 写入 lfu :
	lfu.put(1, 1)                      // lfu.put(1, 1)
	lfu.put(2, 2)                      // lfu.put(2, 2)
	got := []int{}                     // 把 []int{} 写入 got :
	got = append(got, lfu.get(1))      // 把 append(got, lfu 查找 1)) 写入 got
	lfu.put(3, 3)                      // lfu.put(3, 3)
	got = append(got, lfu.get(2))      // 把 append(got, lfu 查找 2)) 写入 got
	got = append(got, lfu.get(3))      // 把 append(got, lfu 查找 3)) 写入 got
	lfu.put(4, 4)                      // lfu.put(4, 4)
	got = append(got, lfu.get(1))      // 把 append(got, lfu 查找 1)) 写入 got
	got = append(got, lfu.get(3))      // 把 append(got, lfu 查找 3)) 写入 got
	got = append(got, lfu.get(4))      // 把 append(got, lfu 查找 4)) 写入 got
	want := []int{1, -1, 3, -1, 3, 4}  // 把 []int{1, 减 1, 3, 减 1, 3, 4} 写入 want :
	if !reflect.DeepEqual(got, want) { // 若 取反 reflect.DeepEqual(got, want
		fmt.Printf("FAIL LFU %v want %v\n", got, want) // 打印输出
		os.Exit(1)                                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
