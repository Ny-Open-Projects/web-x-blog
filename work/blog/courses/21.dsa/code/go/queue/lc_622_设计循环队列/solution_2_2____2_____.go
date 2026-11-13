// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type MyCircularQueue struct { // 定义类型
	capacity int   // capacity int
	data     []int // data []int
	front    int   // front int
	rear     int   // rear int
	size     int   // 大小 int
}

func NewMyCircularQueue(k int) *MyCircularQueue { // 定义函数/方法 NewMyCircularQueue
	return &MyCircularQueue{capacity: k, data: make([]int, k), front: 0, rear: 0, size: 0}
}

func (q *MyCircularQueue) enQueue(value int) bool { // 定义函数/方法 enQueue
	if q.isFull() { // 若 节点.isFull(
		return false // 返回 false
	}
	q.data[q.rear] = value             // 把 value 写入 q.data[q.rear]
	q.rear = (q.rear + 1) % q.capacity // 把 (节点.rear 加 1) 对…取模 节点.capacity 写入 q.rear
	q.size++                           // 节点.大小 加一
	return true                        // 返回 true
}

func (q *MyCircularQueue) deQueue() bool { // 定义函数/方法 deQueue
	if q.isEmpty() { // 若 节点.isEmpty(
		return false // 返回 false
	}
	q.front = (q.front + 1) % q.capacity // 把 (节点.front 加 1) 对…取模 节点.capacity 写入 q.front
	q.size--                             // 节点.大小 减一
	return true                          // 返回 true
}

func (q *MyCircularQueue) frontVal() int { // 定义函数/方法 frontVal
	if q.isEmpty() { // 若 节点.isEmpty(
		return -1 // 返回 减 1
	}
	return q.data[q.front] // 返回 节点.data[节点.front]
}

func (q *MyCircularQueue) rearVal() int { // 定义函数/方法 rearVal
	if q.isEmpty() { // 若 节点.isEmpty(
		return -1 // 返回 减 1
	}
	return q.data[(q.rear-1+q.capacity)%q.capacity] // 返回 节点.data[(节点.rear 减 1 加 节点.capacity) 对…取模 节点.capacity]
}

func (q *MyCircularQueue) isEmpty() bool { return q.size == 0 }          // 定义判定函数 isEmpty
func (q *MyCircularQueue) isFull() bool  { return q.size == q.capacity } // 定义判定函数 isFull

func main() { // 程序入口：跑内嵌自测用例
	q := NewMyCircularQueue(3) // 把 NewMyCircularQueue(3) 写入 q :
	ok := true                 // 把 true 写入 ok :
	checks := []bool{          // 把 []bool{ 写入 checks :
		q.enQueue(1) == true,
		q.enQueue(2) == true,
		q.enQueue(3) == true,
		q.enQueue(4) == false,
		q.rearVal() == 3,
		q.isFull() == true,
		q.deQueue() == true,
		q.enQueue(4) == true,
		q.rearVal() == 4,
	}
	for i, c := range checks { // 同时取 下标 i 与 字符 遍历
		if !c { // 若 取反 字符
			ok = false                      // 把 false 写入 ok
			fmt.Printf("FAIL step %d\n", i) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
