// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134097112
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type LRUCache struct { // 定义类型
	length int         // 长度 int
	data   map[int]int // data 映射表[int]int
	order  []int       // order []int
}

func NewLRU(length int) *LRUCache { // 定义函数/方法 NewLRU
	return &LRUCache{length: length, data: make(map[int]int)} // 返回 按位与 LRUCache{长度: 长度, data: make(映射表[int]int)}
}

func (c *LRUCache) set(key, value int) { // 定义函数/方法 set
	if _, ok := c.data[key]; ok { // 若 _, ok : 赋值为 字符.data[key]; ok
		for i, k := range c.order { // 同时取 下标 i 与 下标 k 遍历
			if k == key { // 若 下标 k 等于 key
				c.order = append(c.order[:i], c.order[i+1:]...) // 把 append(字符.order[:下标 i], 字符.order[下标 i 加 1:]...) 写入 c.order
				break                                           // 跳出循环
			}
		}
	}
	c.data[key] = value            // 把 value 写入 c.data[key]
	c.order = append(c.order, key) // 把 append(字符.order, key) 写入 c.order
	if len(c.data) > c.length {    // 若 长度(字符.data) 超过 字符.长度
		delKey := c.order[0]   // 把 字符.order[0] 写入 delKey :
		c.order = c.order[1:]  // 把 字符.order[1:] 写入 c.order
		delete(c.data, delKey) // delete(字符.data, delKey)
	}
}

func (c *LRUCache) get(key int) (int, bool) { // 定义函数/方法 get
	if _, ok := c.data[key]; !ok { // 若 _, ok : 赋值为 字符.data[key]; 取反 ok
		return 0, false // 返回 0, false
	}
	value := c.data[key]        // 把 字符.data[key] 写入 value :
	for i, k := range c.order { // 同时取 下标 i 与 下标 k 遍历
		if k == key { // 若 下标 k 等于 key
			c.order = append(c.order[:i], c.order[i+1:]...) // 把 append(字符.order[:下标 i], 字符.order[下标 i 加 1:]...) 写入 c.order
			break                                           // 跳出循环
		}
	}
	c.order = append(c.order, key) // 把 append(字符.order, key) 写入 c.order
	return value, true             // 返回 value, true
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
