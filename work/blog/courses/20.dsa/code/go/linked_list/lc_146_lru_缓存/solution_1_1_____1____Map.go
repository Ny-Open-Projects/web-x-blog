// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094527
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

type LRUCache struct { // 定义类型
	capacity int         // capacity int
	cache    map[int]int // cache 映射表[int]int
	order    []int       // order []int
}

func Constructor(capacity int) LRUCache { // 定义函数/方法 Constructor
	return LRUCache{capacity: capacity, cache: make(map[int]int)} // 返回 LRUCache{capacity: capacity, cache: make(映射表[int]int)}
}

func (this *LRUCache) removeFromOrder(key int) { // 定义函数/方法 removeFromOrder
	for i, k := range this.order { // 同时取 下标 i 与 下标 k 遍历
		if k == key { // 若 下标 k 等于 key
			this.order = append(this.order[:i], this.order[i+1:]...)
			return // return
		}
	}
}

func (this *LRUCache) Get(key int) int { // 定义函数/方法 Get
	if _, ok := this.cache[key]; !ok { // 若 _, ok : 赋值为 this.cache[key]; 取反 ok
		return -1 // 返回 减 1
	}
	this.removeFromOrder(key)            // this.removeFromOrder(key)
	this.order = append(this.order, key) // 把 append(this.order, key) 写入 this.order
	return this.cache[key]               // 返回 this.cache[key]
}

func (this *LRUCache) Put(key int, value int) { // 定义函数/方法 Put
	if _, ok := this.cache[key]; ok { // 若 _, ok : 赋值为 this.cache[key]; ok
		delete(this.cache, key)   // delete(this.cache, key)
		this.removeFromOrder(key) // this.removeFromOrder(key)
	} else if len(this.cache) >= this.capacity { // 否则，若 长度(this.cache) 不低于 this.capacity
		oldest := this.order[0]     // 把 this.order[0] 写入 oldest :
		this.order = this.order[1:] // 把 this.order[1:] 写入 this.order
		delete(this.cache, oldest)  // delete(this.cache, oldest)
	}
	this.cache[key] = value              // 把 value 写入 this.cache[key]
	this.order = append(this.order, key) // 把 append(this.order, key) 写入 this.order
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
