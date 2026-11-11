// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func absInt2(x int) int { // 定义函数/方法 absInt2
	if x < 0 { // 若 x 小于 0
		return -x // 返回 减 x
	}
	return x // 返回 x
}

// faithful translation of python solution_4___4.py
// 八皇后问题（栈/迭代回溯）：用显式栈代替递归，按列放置皇后并通过 valid 检查安全性。
func nQueensStack() [][]int { // 定义函数/方法 nQueensStack
	valid := func(x int, a []int) bool { // 把 func(x int, 数组 []int) bool { 写入 valid :
		y := len(a) + 1          // 把 长度(数组) 加 1 写入 y :
		for i := 1; i < y; i++ { // 让 下标 i 从 1 开始计数
			if x == a[i-1] || absInt2(y-i) == absInt2(x-a[i-1]) {
				return false // 返回 false
			}
		}
		return true // 返回 true
	}
	solutions := [][]int{} // 把 [][]int{} 写入 solutions :
	stack := [][]int{{}}   // 把 [][]int{{}} 写入 stack :
	for len(stack) > 0 {   // for 长度(栈) 超过 0 {
		a := stack[len(stack)-1]     // 把 栈[长度(栈) 减 1] 写入 a :
		stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
		if len(a) == 8 {             // 若 长度(数组) 等于 8
			cp := make([]int, 8)              // 把 make([]int, 8) 写入 cp :
			copy(cp, a)                       // copy(cp, 数组)
			solutions = append(solutions, cp) // 把 append(solutions, cp) 写入 solutions
		} else { // 否则
			for i := 1; i <= 8; i++ { // 让 下标 i 从 1 开始计数
				if valid(i, a) { // 定义函数/方法 valid
					nxt := make([]int, len(a), len(a)+1) // 把 make([]int, 长度(数组), 长度(数组) 加 1) 写入 nxt :
					copy(nxt, a)                         // copy(nxt, 数组)
					nxt = append(nxt, i)                 // 追加新元素
					stack = append(stack, nxt)           // 把 append(栈, nxt) 写入 栈
				}
			}
		}
	}
	return solutions // 返回 solutions
}

func main() { // 程序入口：跑内嵌自测用例
	sols := nQueensStack() // 把 nQueensStack() 写入 sols :
	ok := true             // 把 true 写入 ok :
	if len(sols) != 92 {   // 若 长度(sols) 不等于 92
		ok = false                                                    // 把 false 写入 ok
		fmt.Printf("FAIL nQueensStack count=%d want 92\n", len(sols)) // 打印输出
	}
	if len(sols) >= 1 && fmt.Sprint(sols[0]) != "[8 4 1 3 6 2 7 5]" {
		ok = false                                                                 // 把 false 写入 ok
		fmt.Printf("FAIL nQueensStack first=%v want [8 4 1 3 6 2 7 5]\n", sols[0]) // 打印输出
	}
	if len(sols) >= 2 && fmt.Sprint(sols[len(sols)-1]) != "[1 5 8 6 3 7 2 4]" {
		ok = false                                                                          // 把 false 写入 ok
		fmt.Printf("FAIL nQueensStack last=%v want [1 5 8 6 3 7 2 4]\n", sols[len(sols)-1]) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
