// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145245934
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type MinStack struct { // 定义类型
	stack []int // 栈 []int
	mins  []int // mins []int
}

func NewMinStack() *MinStack { // 定义函数/方法 NewMinStack
	return &MinStack{[]int{}, []int{}} // 返回 按位与 MinStack{[]int{}, []int{}}
}

func (s *MinStack) push(val int) { // 定义函数/方法 push
	s.stack = append(s.stack, val) // 把 append(字符串.栈, 值) 写入 栈
	var m int                      // var 映射表 int
	if len(s.mins) > 0 {           // 若 长度(字符串.mins) 超过 0
		if s.mins[len(s.mins)-1] < val { // 若 字符串.mins[长度(字符串.mins) 减 1] 小于 值
			m = s.mins[len(s.mins)-1] // 把 字符串.mins[长度(字符串.mins) 减 1] 写入 映射表
		} else { // 否则
			m = val // 把 值 写入 映射表
		}
	} else { // 否则
		m = val // 把 值 写入 映射表
	}
	s.mins = append(s.mins, m) // 把 append(字符串.mins, 映射表) 写入 s.mins
}

func (s *MinStack) pop() { // 定义函数/方法 pop
	s.stack = s.stack[:len(s.stack)-1] // 把 字符串.栈[:长度(字符串.栈) 减 1] 写入 栈
	s.mins = s.mins[:len(s.mins)-1]    // 把 字符串.mins[:长度(字符串.mins) 减 1] 写入 s.mins
}

func (s *MinStack) top() int { // 定义函数/方法 top
	return s.stack[len(s.stack)-1] // 返回 字符串.栈[长度(字符串.栈) 减 1]
}

func (s *MinStack) getMin() int { // 定义函数/方法 getMin
	return s.mins[len(s.mins)-1] // 返回 字符串.mins[长度(字符串.mins) 减 1]
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
