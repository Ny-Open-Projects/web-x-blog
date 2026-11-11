// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145113825
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type MyStack struct { // 定义类型
	queue1 []int // queue1 []int
	queue2 []int // queue2 []int
}

func NewMyStack() *MyStack { // 定义函数/方法 NewMyStack
	return &MyStack{} // 返回 按位与 MyStack{}
}

func (s *MyStack) push(x int) { // 定义函数/方法 push
	s.queue2 = append(s.queue2, x) // 把 append(字符串.queue2, x) 写入 s.queue2
	for len(s.queue1) > 0 {        // for 长度(字符串.queue1) 超过 0 {
		s.queue2 = append(s.queue2, s.queue1[0]) // 把 append(字符串.queue2, 字符串.queue1[0]) 写入 s.queue2
		s.queue1 = s.queue1[1:]                  // 把 字符串.queue1[1:] 写入 s.queue1
	}
	s.queue1, s.queue2 = s.queue2, s.queue1 // 把 字符串.queue2, 字符串.queue1 写入 s.queue1, s.queue2
}

func (s *MyStack) pop() int { // 定义函数/方法 pop
	val := s.queue1[0]      // 把 字符串.queue1[0] 写入 val :
	s.queue1 = s.queue1[1:] // 把 字符串.queue1[1:] 写入 s.queue1
	return val              // 返回 值
}

func (s *MyStack) top() int { // 定义函数/方法 top
	return s.queue1[0] // 返回 字符串.queue1[0]
}

func (s *MyStack) empty() bool { // 定义函数/方法 empty
	return len(s.queue1) == 0 // 返回 长度(字符串.queue1) 等于 0
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                  // 把 true 写入 ok :
	obj := NewMyStack()         // 把 NewMyStack() 写入 obj :
	obj.push(1)                 // 把 1 压入栈/数组尾部
	obj.push(2)                 // 把 2 压入栈/数组尾部
	if v := obj.top(); v != 2 { // 若 值 : 赋值为 obj.top(); 值 不等于 2
		ok = false                            // 把 false 写入 ok
		fmt.Printf("FAIL top=%v want 2\n", v) // 打印输出
	}
	if v := obj.pop(); v != 2 { // 若 值 : 赋值为 obj 弹出 ); 值 不等于 2
		ok = false                            // 把 false 写入 ok
		fmt.Printf("FAIL pop=%v want 2\n", v) // 打印输出
	}
	if v := obj.empty(); v != false { // 若 值 : 赋值为 obj 是否为空; 值 不等于 false
		ok = false                                  // 把 false 写入 ok
		fmt.Printf("FAIL empty=%v want false\n", v) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
