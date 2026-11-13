// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130471048
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type MyCircularQueue struct { // 定义类型
	queue    []int // 队列 []int
	front    int   // front int
	rear     int   // rear int
	size     int   // 大小 int
	capacity int   // capacity int
}

func NewMyCircularQueue(k int) *MyCircularQueue { // 定义函数/方法 NewMyCircularQueue
	return &MyCircularQueue{queue: make([]int, k), front: 0, rear: -1, size: 0, capacity: k}
}

func (q *MyCircularQueue) enQueue(value int) bool { // 定义函数/方法 enQueue
	if q.isFull() { // 若 节点.isFull(
		return false // 返回 false
	}
	q.rear = (q.rear + 1) % q.capacity // 把 (节点.rear 加 1) 对…取模 节点.capacity 写入 q.rear
	q.queue[q.rear] = value            // 把 value 写入 q.queue[q.rear]
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

func (q *MyCircularQueue) Front() int { // 定义函数/方法 Front
	if q.isEmpty() { // 若 节点.isEmpty(
		return -1 // 返回 减 1
	}
	return q.queue[q.front] // 返回 节点.队列[节点.front]
}

func (q *MyCircularQueue) Rear() int { // 定义函数/方法 Rear
	if q.isEmpty() { // 若 节点.isEmpty(
		return -1 // 返回 减 1
	}
	return q.queue[q.rear] // 返回 节点.队列[节点.rear]
}

func (q *MyCircularQueue) isEmpty() bool { return q.size == 0 }          // 定义判定函数 isEmpty
func (q *MyCircularQueue) isFull() bool  { return q.size == q.capacity } // 定义判定函数 isFull

func main() { // 程序入口：跑内嵌自测用例
	q := NewMyCircularQueue(3) // 把 NewMyCircularQueue(3) 写入 q :
	ok := true                 // 把 true 写入 ok :
	if !q.enQueue(1) {         // 若 取反 节点.enQueue(1
		ok = false                   // 把 false 写入 ok
		fmt.Println("FAIL enQueue1") // 打印输出
	}
	if !q.enQueue(2) { // 若 取反 节点.enQueue(2
		ok = false                   // 把 false 写入 ok
		fmt.Println("FAIL enQueue2") // 打印输出
	}
	if q.Rear() != 2 { // 若 节点.Rear() 不等于 2
		ok = false                             // 把 false 写入 ok
		fmt.Printf("FAIL Rear=%d\n", q.Rear()) // 打印输出
	}
	if !q.deQueue() { // 若 取反 节点.deQueue(
		ok = false                  // 把 false 写入 ok
		fmt.Println("FAIL deQueue") // 打印输出
	}
	if q.Front() != 2 { // 若 节点.Front() 不等于 2
		ok = false                               // 把 false 写入 ok
		fmt.Printf("FAIL Front=%d\n", q.Front()) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
