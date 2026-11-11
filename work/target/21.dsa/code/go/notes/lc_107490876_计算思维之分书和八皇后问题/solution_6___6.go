// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// faithful translation of python solution_6___6.py
// 八皇后问题（程序优化 / 函数式不可变状态传递）：每次递归传入新的状态副本。
func nQueensFunc() [][]int { // 定义函数/方法 nQueensFunc
	const SIZE = 8       // 把 8 存入 SIZE
	results := [][]int{} // 把 [][]int{} 写入 results :
	// place(col, state): state = (colRowList, rows, diag1, diag2)
	var place func(col int, colRow []int, rows []bool, diag1 []bool, diag2 []bool)
	place = func(col int, colRow []int, rows []bool, diag1 []bool, diag2 []bool) {
		if col == SIZE { // 若 col 等于 SIZE
			cp := make([]int, SIZE)       // 把 make([]int, SIZE) 写入 cp :
			copy(cp, colRow)              // copy(cp, colRow)
			results = append(results, cp) // 把 append(results, cp) 写入 results
			return                        // return
		}
		for row := 0; row < SIZE; row++ { // 让 row 从 0 开始计数
			d1 := col - row + (SIZE - 1)             // 把 col 减 row 加 (SIZE 减 1) 写入 d1 :
			d2 := col + row                          // 把 col 加 row 写入 d2 :
			if rows[row] && diag1[d1] && diag2[d2] { // 若 行数[row] 且 diag1[d1] 且 diag2[d2]
				nr := make([]bool, SIZE)                       // 把 make([]bool, SIZE) 写入 nr :
				copy(nr, rows)                                 // copy(nr, 行数)
				nr[row] = false                                // 把 false 写入 nr[row]
				nd1 := make([]bool, 2*SIZE-1)                  // 把 make([]bool, 2 乘 SIZE 减 1) 写入 nd1 :
				copy(nd1, diag1)                               // copy(nd1, diag1)
				nd1[d1] = false                                // 把 false 写入 nd1[d1]
				nd2 := make([]bool, 2*SIZE-1)                  // 把 make([]bool, 2 乘 SIZE 减 1) 写入 nd2 :
				copy(nd2, diag2)                               // copy(nd2, diag2)
				nd2[d2] = false                                // 把 false 写入 nd2[d2]
				ncr := make([]int, len(colRow), len(colRow)+1) // 把 make([]int, 长度(colRow), 长度(colRow) 加 1) 写入 ncr :
				copy(ncr, colRow)                              // copy(ncr, colRow)
				ncr = append(ncr, row)                         // 把 append(ncr, row) 写入 ncr
				place(col+1, ncr, nr, nd1, nd2)                // place(col 加 1, ncr, nr, nd1, nd2)
			}
		}
	}
	place(0, []int{}, boolsTrue(SIZE), boolsTrue(2*SIZE-1), boolsTrue(2*SIZE-1))
	return results // 返回 results
}

func boolsTrue(n int) []bool { // 定义函数/方法 boolsTrue
	b := make([]bool, n) // 把 make([]bool, 元素个数) 写入 b :
	for i := range b {   // 把 range b { 写入 for i :
		b[i] = true // 把 true 写入 b[i]
	}
	return b // 返回 b
}

func main() { // 程序入口：跑内嵌自测用例
	sols := nQueensFunc() // 把 nQueensFunc() 写入 sols :
	ok := true            // 把 true 写入 ok :
	if len(sols) != 92 {  // 若 长度(sols) 不等于 92
		ok = false                                                   // 把 false 写入 ok
		fmt.Printf("FAIL nQueensFunc count=%d want 92\n", len(sols)) // 打印输出
	}
	if len(sols) >= 1 && fmt.Sprint(sols[0]) != "[0 4 7 5 2 6 1 3]" {
		ok = false                                                                // 把 false 写入 ok
		fmt.Printf("FAIL nQueensFunc first=%v want [0 4 7 5 2 6 1 3]\n", sols[0]) // 打印输出
	}
	if len(sols) >= 2 && fmt.Sprint(sols[len(sols)-1]) != "[7 3 0 2 5 1 6 4]" {
		ok = false                                                                         // 把 false 写入 ok
		fmt.Printf("FAIL nQueensFunc last=%v want [7 3 0 2 5 1 6 4]\n", sols[len(sols)-1]) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
