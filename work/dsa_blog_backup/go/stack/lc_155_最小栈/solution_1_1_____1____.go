// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
package main // 引入依赖

import (
	"fmt"  // 「fmt」
	"math" // 「math」
	"os"   // 「os」
)

type MinStack struct { // 定义类型
	xStack   []int // xStack []int
	minStack []int // minStack []int
}

func NewMinStack() *MinStack { // 定义函数/方法 NewMinStack
	return &MinStack{[]int{}, []int{math.MaxInt}} // 返回 按位与 MinStack{[]int{}, []int{math.MaxInt}}
}

func (s *MinStack) push(val int) { // 定义函数/方法 push
	s.xStack = append(s.xStack, val)    // 把 append(字符串.xStack, 值) 写入 s.xStack
	mi := s.minStack[len(s.minStack)-1] // 把 字符串.minStack[长度(字符串.minStack) 减 1] 写入 mi :
	if val < mi {                       // 若 值 小于 mi
		mi = val // 把 值 写入 mi
	}
	s.minStack = append(s.minStack, mi) // 把 append(字符串.minStack, mi) 写入 s.minStack
}

func (s *MinStack) pop() { // 定义函数/方法 pop
	s.xStack = s.xStack[:len(s.xStack)-1]       // 把 字符串.xStack[:长度(字符串.xStack) 减 1] 写入 s.xStack
	s.minStack = s.minStack[:len(s.minStack)-1] // 把 字符串.minStack[:长度(字符串.minStack) 减 1] 写入 s.minStack
}

func (s *MinStack) top() int { // 定义函数/方法 top
	return s.xStack[len(s.xStack)-1] // 返回 字符串.xStack[长度(字符串.xStack) 减 1]
}

func (s *MinStack) getMin() int { // 定义函数/方法 getMin
	return s.minStack[len(s.minStack)-1] // 返回 字符串.minStack[长度(字符串.minStack) 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                     // 把 true 写入 ok :
	ms := NewMinStack()            // 把 NewMinStack() 写入 ms :
	ms.push(-2)                    // 把 减 2 压入栈/数组尾部
	ms.push(0)                     // 把 0 压入栈/数组尾部
	ms.push(-3)                    // 把 减 3 压入栈/数组尾部
	if v := ms.getMin(); v != -3 { // 若 值 : 赋值为 ms.getMin(); 值 不等于 减 3
		ok = false                                // 把 false 写入 ok
		fmt.Printf("FAIL getMin=%v want -3\n", v) // 打印输出
	}
	ms.pop()                   // 弹出栈顶元素
	if v := ms.top(); v != 0 { // 若 值 : 赋值为 ms.top(); 值 不等于 0
		ok = false                            // 把 false 写入 ok
		fmt.Printf("FAIL top=%v want 0\n", v) // 打印输出
	}
	if v := ms.getMin(); v != -2 { // 若 值 : 赋值为 ms.getMin(); 值 不等于 减 2
		ok = false                                 // 把 false 写入 ok
		fmt.Printf("FAIL getMin2=%v want -2\n", v) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
