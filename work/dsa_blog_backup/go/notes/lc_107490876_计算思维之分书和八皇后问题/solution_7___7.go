// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func absInt3(x int) int { // 定义函数/方法 absInt3
	if x < 0 { // 若 x 小于 0
		return -x // 返回 减 x
	}
	return x // 返回 x
}

// faithful translation of python solution_7___7.py
// 八皇后问题（简洁递归版）：以 (row, col) 记录已放置皇后，逐列尝试并检查攻击。
func nQueensSimple() [][]int { // 定义函数/方法 nQueensSimple
	type pos struct{ r, c int }   // 定义类型
	positions := []pos{}          // 把 []pos{} 写入 positions :
	solutions := [][]int{}        // 把 [][]int{} 写入 solutions :
	safe := func(r, c int) bool { // 把 func(右指针, 字符 int) bool { 写入 safe :
		for _, p := range positions { // 同时取 _ 与 节点 遍历
			if p.r == r || absInt3(p.r-r) == absInt3(p.c-c) {
				return false // 返回 false
			}
		}
		return true // 返回 true
	}
	var solve func(col int) // var solve func(col int)
	solve = func(col int) { // 把 func(col int) { 写入 solve
		if col == 8 { // 若 col 等于 8
			s := make([]int, 8)           // 把 make([]int, 8) 写入 s :
			for i, p := range positions { // 同时取 下标 i 与 节点 遍历
				s[i] = p.r // 把 节点.右指针 写入 s[i]
			}
			solutions = append(solutions, s) // 把 append(solutions, 字符串) 写入 solutions
			return                           // return
		}
		for r := 0; r < 8; r++ { // 让 右指针 从 0 开始计数
			if safe(r, col) { // 定义函数/方法 safe
				positions = append(positions, pos{r, col}) // 把 append(positions, pos{右指针, col}) 写入 positions
				solve(col + 1)                             // solve(col 加 1)
				positions = positions[:len(positions)-1]   // 把 positions[:长度(positions) 减 1] 写入 positions
			}
		}
	}
	solve(0)         // solve(0)
	return solutions // 返回 solutions
}

func main() { // 程序入口：跑内嵌自测用例
	sols := nQueensSimple() // 把 nQueensSimple() 写入 sols :
	ok := true              // 把 true 写入 ok :
	if len(sols) != 92 {    // 若 长度(sols) 不等于 92
		ok = false                                                     // 把 false 写入 ok
		fmt.Printf("FAIL nQueensSimple count=%d want 92\n", len(sols)) // 打印输出
	}
	if len(sols) >= 1 && fmt.Sprint(sols[0]) != "[0 4 7 5 2 6 1 3]" {
		ok = false                                                                  // 把 false 写入 ok
		fmt.Printf("FAIL nQueensSimple first=%v want [0 4 7 5 2 6 1 3]\n", sols[0]) // 打印输出
	}
	if len(sols) >= 2 && fmt.Sprint(sols[len(sols)-1]) != "[7 3 0 2 5 1 6 4]" {
		ok = false                                                                           // 把 false 写入 ok
		fmt.Printf("FAIL nQueensSimple last=%v want [7 3 0 2 5 1 6 4]\n", sols[len(sols)-1]) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
