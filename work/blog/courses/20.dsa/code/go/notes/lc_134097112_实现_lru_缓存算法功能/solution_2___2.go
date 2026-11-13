// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
package main // 引入依赖

import (
	"container/list" // 「container 除以 列表」
	"fmt"            // 「fmt」
	"os"             // 「os」
)

type entry struct { // 定义类型
	key   int // key int
	value int // value int
}

type LRUCache struct { // 定义类型
	capacity int                   // capacity int
	ll       *list.List            // ll 乘 列表.List
	items    map[int]*list.Element // items 映射表[int] 乘 列表.Element
}

func NewLRU(capacity int) *LRUCache { // 定义函数/方法 NewLRU
	return &LRUCache{capacity: capacity, ll: list.New(), items: make(map[int]*list.Element)}
}

func (c *LRUCache) get(key int) (int, bool) { // 定义函数/方法 get
	if el, ok := c.items[key]; ok { // 若 el, ok : 赋值为 字符.items[key]; ok
		c.ll.MoveToFront(el)                 // 字符.ll.MoveToFront(el)
		return el.Value.(*entry).value, true // 返回 el.Value.( 乘 entry).value, true
	}
	return 0, false // 返回 0, false
}

func (c *LRUCache) set(key, value int) { // 定义函数/方法 set
	if el, ok := c.items[key]; ok { // 若 el, ok : 赋值为 字符.items[key]; ok
		c.ll.MoveToFront(el)            // 字符.ll.MoveToFront(el)
		el.Value.(*entry).value = value // 把 value 写入 el.Value.(*entry).value
		return                          // return
	}
	el := c.ll.PushFront(&entry{key, value}) // 把 字符.ll.PushFront( 按位与 entry{key, value}) 写入 el :
	c.items[key] = el                        // 把 el 写入 c.items[key]
	if c.ll.Len() > c.capacity {             // 若 字符.ll.Len() 超过 字符.capacity
		back := c.ll.Back() // 把 字符.ll.Back() 写入 back :
		if back != nil {    // 若 back 不等于 nil
			c.ll.Remove(back)                        // 字符.ll.Remove(back)
			delete(c.items, back.Value.(*entry).key) // delete(字符.items, back.Value.( 乘 entry).key)
		}
	}
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
