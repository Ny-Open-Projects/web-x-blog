// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// sortStackTwoStacks 用两个栈对栈排序（升序，栈顶最大）：
// 主栈逐个弹出，借助辅助栈把所有比当前元素大的都压回主栈，再把当前元素压入辅助栈。
func sortStackTwoStacks(stack []int) []int { // 定义函数/方法 sortStackTwoStacks
	aux := []int{}       // 把 []int{} 写入 aux :
	for len(stack) > 0 { // for 长度(栈) 超过 0 {
		top := stack[len(stack)-1]                  // 把 栈[长度(栈) 减 1] 写入 top :
		stack = stack[:len(stack)-1]                // 把 栈[:长度(栈) 减 1] 写入 栈
		for len(aux) > 0 && aux[len(aux)-1] > top { // for 长度(aux) 超过 0 且 aux[长度(aux) 减 1] 超过 top {
			stack = append(stack, aux[len(aux)-1]) // 把 append(栈, aux[长度(aux) 减 1]) 写入 栈
			aux = aux[:len(aux)-1]                 // 把 aux[:长度(aux) 减 1] 写入 aux
		}
		aux = append(aux, top) // 把 append(aux, top) 写入 aux
	}
	return aux // 返回 aux
}

func eqIntSlice(a, b []int) bool { // 定义函数/方法 eqIntSlice
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	for i := range a { // 把 range 数组 { 写入 for i :
		if a[i] != b[i] { // 若 数组[下标 i] 不等于 b[下标 i]
			return false // 返回 false
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want []int // want []int
	}{ // }{
		{[]int{1, 3, 2, 4}, []int{1, 2, 3, 4}},
		{[]int{3, 1, 4, 2}, []int{1, 2, 3, 4}},
		{[]int{}, []int{}},
		{[]int{5}, []int{5}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := sortStackTwoStacks(c.in); !eqIntSlice(got, c.want) {
			ok = false                                                                // 把 false 写入 ok
			fmt.Printf("FAIL sortStackTwoStacks(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
