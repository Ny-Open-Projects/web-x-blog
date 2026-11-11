// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397311
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

type SortedStack struct { // 定义类型
	stk []int // 栈 []int
}

func Constructor() SortedStack { // 定义函数/方法 Constructor
	return SortedStack{stk: []int{}} // 返回 SortedStack{栈: []int{}}
}

func (this *SortedStack) Push(val int) { // 定义函数/方法 Push
	tempStack := []int{}                                       // 把 []int{} 写入 tempStack :
	for len(this.stk) > 0 && this.stk[len(this.stk)-1] > val { // for 长度(this.栈) 超过 0 且 this.栈[长度(this.栈) 减 1] 超过 值 {
		tempStack = append(tempStack, this.stk[len(this.stk)-1]) // 把 append(tempStack, this.栈[长度(this.栈) 减 1]) 写入 tempStack
		this.stk = this.stk[:len(this.stk)-1]                    // 把 this.栈[:长度(this.栈) 减 1] 写入 栈
	}
	this.stk = append(this.stk, val) // 把 append(this.栈, 值) 写入 栈
	for len(tempStack) > 0 {         // for 长度(tempStack) 超过 0 {
		this.stk = append(this.stk, tempStack[len(tempStack)-1]) // 把 append(this.栈, tempStack[长度(tempStack) 减 1]) 写入 栈
		tempStack = tempStack[:len(tempStack)-1]                 // 把 tempStack[:长度(tempStack) 减 1] 写入 tempStack
	}
}

func (this *SortedStack) Pop() { // 定义函数/方法 Pop
	if !this.IsEmpty() { // 若 取反 this.IsEmpty(
		this.stk = this.stk[:len(this.stk)-1] // 把 this.栈[:长度(this.栈) 减 1] 写入 栈
	}
}

func (this *SortedStack) Peek() int { // 定义函数/方法 Peek
	if this.IsEmpty() { // 若 this.IsEmpty(
		return -1 // 返回 减 1
	}
	return this.stk[len(this.stk)-1] // 返回 this.栈[长度(this.栈) 减 1]
}

func (this *SortedStack) IsEmpty() bool { // 定义函数/方法 IsEmpty
	return len(this.stk) == 0 // 返回 长度(this.栈) 等于 0
}

func main() { // 程序入口：跑内嵌自测用例
	s := Constructor()                       // 把 Constructor() 写入 s :
	for _, v := range []int{4, 2, 5, 1, 3} { // 同时取 _ 与 值 遍历
		s.Push(v) // 字符串.Push(值)
	}
	var out []int      // var out []int
	for !s.IsEmpty() { // for 取反 字符串.IsEmpty() {
		out = append(out, s.Peek()) // 把 append(out, 字符串.Peek()) 写入 out
		s.Pop()                     // 字符串.Pop()
	}
	want := []int{5, 4, 3, 2, 1}       // 把 []int{5, 4, 3, 2, 1} 写入 want :
	if !reflect.DeepEqual(out, want) { // 若 取反 reflect.DeepEqual(out, want
		fmt.Println("FAIL", out) // 打印输出
		return                   // return
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
