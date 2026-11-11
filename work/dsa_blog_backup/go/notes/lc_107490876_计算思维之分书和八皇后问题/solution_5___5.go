// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// faithful translation of python solution_5___5.py
// 八皇后问题（优化回溯，rows/diag1/diag2 布尔数组标记），0-indexed。
func nQueensBool() [][]int { // 定义函数/方法 nQueensBool
	const SIZE = 8                  // 把 8 存入 SIZE
	colRow := make([]int, SIZE)     // 把 make([]int, SIZE) 写入 colRow :
	rows := make([]bool, SIZE)      // 把 make([]bool, SIZE) 写入 rows :
	diag1 := make([]bool, 2*SIZE-1) // col - row + OFFSET
	diag2 := make([]bool, 2*SIZE-1) // col + row
	const OFFSET = SIZE - 1         // 把 SIZE 减 1 存入 OFFSET
	for i := range rows {           // 把 range 行数 { 写入 for i :
		rows[i] = true // 把 true 写入 rows[i]
	}
	for i := range diag1 { // 把 range diag1 { 写入 for i :
		diag1[i] = true // 把 true 写入 diag1[i]
		diag2[i] = true // 把 true 写入 diag2[i]
	}
	results := [][]int{}    // 把 [][]int{} 写入 results :
	var place func(col int) // var place func(col int)
	place = func(col int) { // 把 func(col int) { 写入 place
		if col == SIZE { // 若 col 等于 SIZE
			cp := make([]int, SIZE)       // 把 make([]int, SIZE) 写入 cp :
			copy(cp, colRow)              // copy(cp, colRow)
			results = append(results, cp) // 把 append(results, cp) 写入 results
			return                        // return
		}
		for row := 0; row < SIZE; row++ { // 让 row 从 0 开始计数
			d1 := col - row + OFFSET                 // 把 col 减 row 加 OFFSET 写入 d1 :
			d2 := col + row                          // 把 col 加 row 写入 d2 :
			if rows[row] && diag1[d1] && diag2[d2] { // 若 行数[row] 且 diag1[d1] 且 diag2[d2]
				colRow[col] = row // 把 row 写入 colRow[col]
				rows[row] = false // 把 false 写入 rows[row]
				diag1[d1] = false // 把 false 写入 diag1[d1]
				diag2[d2] = false // 把 false 写入 diag2[d2]
				place(col + 1)    // place(col 加 1)
				rows[row] = true  // 把 true 写入 rows[row]
				diag1[d1] = true  // 把 true 写入 diag1[d1]
				diag2[d2] = true  // 把 true 写入 diag2[d2]
			}
		}
	}
	place(0)       // place(0)
	return results // 返回 results
}

func main() { // 程序入口：跑内嵌自测用例
	sols := nQueensBool() // 把 nQueensBool() 写入 sols :
	ok := true            // 把 true 写入 ok :
	if len(sols) != 92 {  // 若 长度(sols) 不等于 92
		ok = false                                                   // 把 false 写入 ok
		fmt.Printf("FAIL nQueensBool count=%d want 92\n", len(sols)) // 打印输出
	}
	if len(sols) >= 1 && fmt.Sprint(sols[0]) != "[0 4 7 5 2 6 1 3]" {
		ok = false                                                                // 把 false 写入 ok
		fmt.Printf("FAIL nQueensBool first=%v want [0 4 7 5 2 6 1 3]\n", sols[0]) // 打印输出
	}
	if len(sols) >= 2 && fmt.Sprint(sols[len(sols)-1]) != "[7 3 0 2 5 1 6 4]" {
		ok = false                                                                         // 把 false 写入 ok
		fmt.Printf("FAIL nQueensBool last=%v want [7 3 0 2 5 1 6 4]\n", sols[len(sols)-1]) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
