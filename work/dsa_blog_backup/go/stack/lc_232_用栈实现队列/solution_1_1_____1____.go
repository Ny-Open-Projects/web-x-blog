// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145114011
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type MyQueue struct { // 定义类型
	inStack  []int // inStack []int
	outStack []int // outStack []int
}

func NewMyQueue() *MyQueue { // 定义函数/方法 NewMyQueue
	return &MyQueue{} // 返回 按位与 MyQueue{}
}

func (q *MyQueue) push(x int) { // 定义函数/方法 push
	q.inStack = append(q.inStack, x) // 把 append(节点.inStack, x) 写入 q.inStack
}

func (q *MyQueue) pop() int { // 定义函数/方法 pop
	if len(q.outStack) == 0 { // 若 长度(节点.outStack) 等于 0
		q.in2out() // 节点.in2out()
	}
	val := q.outStack[len(q.outStack)-1]        // 把 节点.outStack[长度(节点.outStack) 减 1] 写入 val :
	q.outStack = q.outStack[:len(q.outStack)-1] // 把 节点.outStack[:长度(节点.outStack) 减 1] 写入 q.outStack
	return val                                  // 返回 值
}

func (q *MyQueue) peek() int { // 定义函数/方法 peek
	if len(q.outStack) == 0 { // 若 长度(节点.outStack) 等于 0
		q.in2out() // 节点.in2out()
	}
	return q.outStack[len(q.outStack)-1] // 返回 节点.outStack[长度(节点.outStack) 减 1]
}

func (q *MyQueue) empty() bool { // 定义函数/方法 empty
	return len(q.outStack) == 0 && len(q.inStack) == 0 // 返回 长度(节点.outStack) 等于 0 且 长度(节点.inStack) 等于 0
}

func (q *MyQueue) in2out() { // 定义函数/方法 in2out
	for len(q.inStack) > 0 { // for 长度(节点.inStack) 超过 0 {
		q.outStack = append(q.outStack, q.inStack[len(q.inStack)-1])
		q.inStack = q.inStack[:len(q.inStack)-1] // 把 节点.inStack[:长度(节点.inStack) 减 1] 写入 q.inStack
	}
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                 // 把 true 写入 ok :
	q := NewMyQueue()          // 把 NewMyQueue() 写入 q :
	q.push(1)                  // 把 1 压入栈/数组尾部
	q.push(2)                  // 把 2 压入栈/数组尾部
	if v := q.peek(); v != 1 { // 若 值 : 赋值为 节点.peek(); 值 不等于 1
		ok = false                             // 把 false 写入 ok
		fmt.Printf("FAIL peek=%v want 1\n", v) // 打印输出
	}
	if v := q.pop(); v != 1 { // 若 值 : 赋值为 节点 弹出 ); 值 不等于 1
		ok = false                            // 把 false 写入 ok
		fmt.Printf("FAIL pop=%v want 1\n", v) // 打印输出
	}
	if v := q.empty(); v != false { // 若 值 : 赋值为 节点 是否为空; 值 不等于 false
		ok = false                                  // 把 false 写入 ok
		fmt.Printf("FAIL empty=%v want false\n", v) // 打印输出
	}
	q.push(3)                 // 把 3 压入栈/数组尾部
	if v := q.pop(); v != 2 { // 若 值 : 赋值为 节点 弹出 ); 值 不等于 2
		ok = false                             // 把 false 写入 ok
		fmt.Printf("FAIL pop2=%v want 2\n", v) // 打印输出
	}
	if v := q.pop(); v != 3 { // 若 值 : 赋值为 节点 弹出 ); 值 不等于 3
		ok = false                             // 把 false 写入 ok
		fmt.Printf("FAIL pop3=%v want 3\n", v) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
