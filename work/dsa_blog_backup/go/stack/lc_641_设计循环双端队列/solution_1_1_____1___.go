// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145385578
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type MyCircularDeque struct { // 定义类型
	capacity int   // capacity int
	front    int   // front int
	rear     int   // rear int
	elements []int // elements []int
}

func NewMyCircularDeque(k int) *MyCircularDeque { // 定义函数/方法 NewMyCircularDeque
	capacity := k + 1 // 把 下标 k 加 1 写入 capacity :
	return &MyCircularDeque{capacity: capacity, front: 0, rear: 0, elements: make([]int, capacity)}
}

func (d *MyCircularDeque) insertFront(value int) bool { // 定义函数/方法 insertFront
	if d.isFull() { // 若 d.isFull(
		return false // 返回 false
	}
	d.front = (d.front - 1 + d.capacity) % d.capacity // 把 (d.front 减 1 加 d.capacity) 对…取模 d.capacity 写入 d.front
	d.elements[d.front] = value                       // 把 value 写入 d.elements[d.front]
	return true                                       // 返回 true
}

func (d *MyCircularDeque) insertLast(value int) bool { // 定义函数/方法 insertLast
	if d.isFull() { // 若 d.isFull(
		return false // 返回 false
	}
	d.elements[d.rear] = value         // 把 value 写入 d.elements[d.rear]
	d.rear = (d.rear + 1) % d.capacity // 把 (d.rear 加 1) 对…取模 d.capacity 写入 d.rear
	return true                        // 返回 true
}

func (d *MyCircularDeque) deleteFront() bool { // 定义函数/方法 deleteFront
	if d.isEmpty() { // 若 d.isEmpty(
		return false // 返回 false
	}
	d.front = (d.front + 1) % d.capacity // 把 (d.front 加 1) 对…取模 d.capacity 写入 d.front
	return true                          // 返回 true
}

func (d *MyCircularDeque) deleteLast() bool { // 定义函数/方法 deleteLast
	if d.isEmpty() { // 若 d.isEmpty(
		return false // 返回 false
	}
	d.rear = (d.rear - 1 + d.capacity) % d.capacity // 把 (d.rear 减 1 加 d.capacity) 对…取模 d.capacity 写入 d.rear
	return true                                     // 返回 true
}

func (d *MyCircularDeque) getFront() int { // 定义函数/方法 getFront
	if d.isEmpty() { // 若 d.isEmpty(
		return -1 // 返回 减 1
	}
	return d.elements[d.front] // 返回 d.elements[d.front]
}

func (d *MyCircularDeque) getRear() int { // 定义函数/方法 getRear
	if d.isEmpty() { // 若 d.isEmpty(
		return -1 // 返回 减 1
	}
	return d.elements[(d.rear-1+d.capacity)%d.capacity] // 返回 d.elements[(d.rear 减 1 加 d.capacity) 对…取模 d.capacity]
}

func (d *MyCircularDeque) isEmpty() bool { // 定义判定函数 isEmpty
	return d.rear == d.front // 返回 d.rear 等于 d.front
}

func (d *MyCircularDeque) isFull() bool { // 定义判定函数 isFull
	return (d.rear+1)%d.capacity == d.front // 返回 (d.rear 加 1) 对…取模 d.capacity 等于 d.front
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
