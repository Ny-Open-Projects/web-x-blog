// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385578
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type MyCircularDeque struct { // 定义类型
	data []int // data []int
	head int   // 头节点 int
	tail int   // 尾节点 int
	size int   // 大小 int
	cap  int   // cap int
}

func NewMyCircularDeque(k int) *MyCircularDeque { // 定义函数/方法 NewMyCircularDeque
	return &MyCircularDeque{data: make([]int, k), head: 0, tail: -1, size: 0, cap: k}
}

func (d *MyCircularDeque) insertFront(value int) bool { // 定义函数/方法 insertFront
	if d.isFull() { // 若 d.isFull(
		return false // 返回 false
	}
	d.head = (d.head - 1 + d.cap) % d.cap // 把 (d.头节点 减 1 加 d.cap) 对…取模 d.cap 写入 头节点
	d.data[d.head] = value                // 把 value 写入 d.data[d.head]
	d.size++                              // d.大小 加一
	return true                           // 返回 true
}

func (d *MyCircularDeque) insertLast(value int) bool { // 定义函数/方法 insertLast
	if d.isFull() { // 若 d.isFull(
		return false // 返回 false
	}
	d.tail = (d.tail + 1) % d.cap // 把 (d.尾节点 加 1) 对…取模 d.cap 写入 尾节点
	d.data[d.tail] = value        // 把 value 写入 d.data[d.tail]
	d.size++                      // d.大小 加一
	return true                   // 返回 true
}

func (d *MyCircularDeque) deleteFront() bool { // 定义函数/方法 deleteFront
	if d.isEmpty() { // 若 d.isEmpty(
		return false // 返回 false
	}
	d.head = (d.head + 1) % d.cap // 把 (d.头节点 加 1) 对…取模 d.cap 写入 头节点
	d.size--                      // d.大小 减一
	return true                   // 返回 true
}

func (d *MyCircularDeque) deleteLast() bool { // 定义函数/方法 deleteLast
	if d.isEmpty() { // 若 d.isEmpty(
		return false // 返回 false
	}
	d.tail = (d.tail - 1 + d.cap) % d.cap // 把 (d.尾节点 减 1 加 d.cap) 对…取模 d.cap 写入 尾节点
	d.size--                              // d.大小 减一
	return true                           // 返回 true
}

func (d *MyCircularDeque) getFront() int { // 定义函数/方法 getFront
	if d.isEmpty() { // 若 d.isEmpty(
		return -1 // 返回 减 1
	}
	return d.data[d.head] // 返回 d.data[d.头节点]
}

func (d *MyCircularDeque) getRear() int { // 定义函数/方法 getRear
	if d.isEmpty() { // 若 d.isEmpty(
		return -1 // 返回 减 1
	}
	return d.data[d.tail] // 返回 d.data[d.尾节点]
}

func (d *MyCircularDeque) isEmpty() bool { // 定义判定函数 isEmpty
	return d.size == 0 // 返回 d.大小 等于 0
}

func (d *MyCircularDeque) isFull() bool { // 定义判定函数 isFull
	return d.size == d.cap // 返回 d.大小 等于 d.cap
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                   // 把 true 写入 ok :
	obj := NewMyCircularDeque(3) // 把 NewMyCircularDeque(3) 写入 obj :
	checks := []bool{            // 把 []bool{ 写入 checks :
		obj.insertLast(1),
		obj.insertLast(2),
		obj.insertFront(3),
		obj.insertFront(4),
		obj.getRear() == 2,
		obj.isFull(),
		obj.deleteLast(),
		obj.insertFront(4),
		obj.getFront() == 4,
	}
	wants := []bool{true, true, true, false, true, true, true, true, true}
	for i := range checks { // 把 range checks { 写入 for i :
		if checks[i] != wants[i] { // 若 checks[下标 i] 不等于 wants[下标 i]
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL step %d got %v want %v\n", i, checks[i], wants[i]) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
