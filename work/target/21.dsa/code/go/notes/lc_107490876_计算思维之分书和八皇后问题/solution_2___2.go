// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// faithful translation of python solution_2___2.py
// 分书问题（优化版 / 函数式状态传递）：每次递归传入新的分配状态副本。
func allocateBooksFunc() [][]int { // 定义函数/方法 allocateBooksFunc
	like := [][]int{ // 把 [][]int{ 写入 like :
		{0, 0, 1, 1, 0},
		{1, 1, 0, 0, 1},
		{0, 1, 1, 0, 1},
		{0, 0, 0, 1, 0},
		{0, 1, 0, 0, 1},
	}
	results := [][]int{}                           // 把 [][]int{} 写入 results :
	var tryAssign func(reader int, assigned []int) // var tryAssign func(reader int, assigned []int)
	tryAssign = func(reader int, assigned []int) { // 把 func(reader int, assigned []int) { 写入 tryAssign
		if reader == 5 { // 若 reader 等于 5
			cp := make([]int, 5)          // 把 make([]int, 5) 写入 cp :
			copy(cp, assigned)            // copy(cp, assigned)
			results = append(results, cp) // 把 append(results, cp) 写入 results
			return                        // return
		}
		for book := 0; book < 5; book++ { // 让 book 从 0 开始计数
			if like[reader][book] == 1 && assigned[book] == -1 { // 若 like[reader][book] 等于 1 且 assigned[book] 等于 减 1
				nxt := make([]int, 5)    // 把 make([]int, 5) 写入 nxt :
				copy(nxt, assigned)      // copy(nxt, assigned)
				nxt[book] = reader       // 把 reader 写入 nxt[book]
				tryAssign(reader+1, nxt) // tryAssign(reader 加 1, nxt)
			}
		}
	}
	tryAssign(0, []int{-1, -1, -1, -1, -1}) // tryAssign(0, []int{ 减 1, 减 1, 减 1, 减 1, 减 1})
	return results                          // 返回 results
}

func main() { // 程序入口：跑内嵌自测用例
	res := allocateBooksFunc() // 把 allocateBooksFunc() 写入 res :
	ok := true                 // 把 true 写入 ok :
	if len(res) != 2 {         // 若 长度(结果) 不等于 2
		ok = false                                                       // 把 false 写入 ok
		fmt.Printf("FAIL allocateBooksFunc count=%d want 2\n", len(res)) // 打印输出
	}
	if len(res) >= 1 && fmt.Sprint(res[0]) != "[1 2 0 3 4]" { // 若 长度(结果) 不低于 1 且 fmt.Sprint(结果[0]) 不等于 「[1 2 0 3 4]」
		ok = false                                                               // 把 false 写入 ok
		fmt.Printf("FAIL allocateBooksFunc first=%v want [1 2 0 3 4]\n", res[0]) // 打印输出
	}
	if len(res) >= 2 && fmt.Sprint(res[1]) != "[1 4 0 3 2]" { // 若 长度(结果) 不低于 2 且 fmt.Sprint(结果[1]) 不等于 「[1 4 0 3 2]」
		ok = false                                                              // 把 false 写入 ok
		fmt.Printf("FAIL allocateBooksFunc last=%v want [1 4 0 3 2]\n", res[1]) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
