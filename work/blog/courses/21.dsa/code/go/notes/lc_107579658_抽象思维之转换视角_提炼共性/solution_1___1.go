// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107579658
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// solveUnified 转换视角、提炼共性：分书问题与八皇后问题抽象为同一类回溯问题。
// queen=false 时分书（5 人 5 书，列=书，行=人，受喜好表约束）；
// queen=true 时八皇后（8x8，所有位置均可放）。
func solveUnified(queen bool) int { // 定义函数/方法 solveUnified
	size := 5  // 把 5 写入 size :
	if queen { // 若 queen
		size = 8 // 把 8 写入 大小
	}
	like := [][]int{ // 把 [][]int{ 写入 like :
		{0, 0, 1, 1, 0},
		{1, 1, 0, 0, 1},
		{0, 1, 1, 0, 1},
		{0, 0, 0, 1, 0},
		{0, 1, 0, 0, 1},
	}
	Q := make([]int, size) // 把 make([]int, 大小) 写入 Q :
	for i := range Q {     // 把 range Q { 写入 for i :
		Q[i] = -1 // 把 减 1 写入 Q[i]
	}
	rows := make([]bool, size) // 把 make([]bool, 大小) 写入 rows :
	for i := range rows {      // 把 range 行数 { 写入 for i :
		rows[i] = true // 把 true 写入 rows[i]
	}
	var diag1, diag2 []bool // var diag1, diag2 []bool
	if queen {              // 若 queen
		diag1 = make([]bool, 2*size-1) // 把 make([]bool, 2 乘 大小 减 1) 写入 diag1
		diag2 = make([]bool, 2*size-1) // 把 make([]bool, 2 乘 大小 减 1) 写入 diag2
		for i := range diag1 {         // 把 range diag1 { 写入 for i :
			diag1[i] = true // 把 true 写入 diag1[i]
			diag2[i] = true // 把 true 写入 diag2[i]
		}
	}
	count := 0 // 把 0 写入 count :

	isValid := func(row, col int) bool { // 把 func(row, col int) bool { 写入 isValid :
		if queen { // 若 queen
			return true // 返回 true
		}
		return like[row][col] == 1 // 返回 like[row][col] 等于 1
	}
	isSafe := func(row, col int) bool { // 把 func(row, col int) bool { 写入 isSafe :
		if queen { // 若 queen
			return rows[row] && diag1[col-row+size-1] && diag2[col+row] // 返回 行数[row] 且 diag1[col 减 row 加 大小 减 1] 且 diag2[col 加 row]
		}
		return rows[row] // 返回 行数[row]
	}

	var place func(col int) // var place func(col int)
	place = func(col int) { // 把 func(col int) { 写入 place
		if col == size { // 若 col 等于 大小
			count++ // 计数 加一
			return  // return
		}
		for row := 0; row < size; row++ { // 让 row 从 0 开始计数
			if !isValid(row, col) { // 若 取反 isValid(row, col
				continue // 跳过本轮，进入下一次
			}
			if !isSafe(row, col) { // 若 取反 isSafe(row, col
				continue // 跳过本轮，进入下一次
			}
			Q[col] = row      // 把 row 写入 Q[col]
			rows[row] = false // 把 false 写入 rows[row]
			if queen {        // 若 queen
				d1 := col - row + size - 1 // 把 col 减 row 加 大小 减 1 写入 d1 :
				d2 := col + row            // 把 col 加 row 写入 d2 :
				diag1[d1] = false          // 把 false 写入 diag1[d1]
				diag2[d2] = false          // 把 false 写入 diag2[d2]
			}
			place(col + 1)   // place(col 加 1)
			rows[row] = true // 把 true 写入 rows[row]
			if queen {       // 若 queen
				d1 := col - row + size - 1 // 把 col 减 row 加 大小 减 1 写入 d1 :
				d2 := col + row            // 把 col 加 row 写入 d2 :
				diag1[d1] = true           // 把 true 写入 diag1[d1]
				diag2[d2] = true           // 把 true 写入 diag2[d2]
			}
		}
	}
	place(0)     // place(0)
	return count // 返回 计数
}

func main() { // 程序入口：跑内嵌自测用例
	books := solveUnified(false) // 把 solveUnified(false) 写入 books :
	queens := solveUnified(true) // 把 solveUnified(true) 写入 queens :
	if books != 2 {              // 若 books 不等于 2
		fmt.Printf("FAIL books=%d want=2\n", books) // 打印输出
		os.Exit(1)                                  // os.Exit(1)
	}
	if queens != 92 { // 若 queens 不等于 92
		fmt.Printf("FAIL queens=%d want=92\n", queens) // 打印输出
		os.Exit(1)                                     // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
