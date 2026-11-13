// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107490876
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func absInt(x int) int { // 定义函数/方法 absInt
	if x < 0 { // 若 x 小于 0
		return -x // 返回 减 x
	}
	return x // 返回 x
}

// faithful translation of python solution_3___3.py
// 八皇后问题（逐列放置 + 显式安全检查 isSafe）：board[col]=row 记录每列皇后所在行（1..8）。
func nQueensSafe() [][]int { // 定义函数/方法 nQueensSafe
	results := [][]int{}                // 把 [][]int{} 写入 results :
	board := make([]int, 8)             // 把 make([]int, 8) 写入 board :
	isSafe := func(col, row int) bool { // 把 func(col, row int) bool { 写入 isSafe :
		for c := 0; c < col; c++ { // 让 字符 从 0 开始计数
			if board[c] == row || absInt(board[c]-row) == absInt(c-col) { // 若 棋盘[字符] 等于 row 或 absInt(棋盘[字符] 减 row) 等于 absInt(字符 减 col
				return false // 返回 false
			}
		}
		return true // 返回 true
	}
	var place func(col int) // var place func(col int)
	place = func(col int) { // 把 func(col int) { 写入 place
		if col == 8 { // 若 col 等于 8
			cp := make([]int, 8)          // 把 make([]int, 8) 写入 cp :
			copy(cp, board)               // copy(cp, 棋盘)
			results = append(results, cp) // 把 append(results, cp) 写入 results
			return                        // return
		}
		for row := 1; row <= 8; row++ { // 让 row 从 1 开始计数
			if isSafe(col, row) { // 定义判定函数 isSafe
				board[col] = row // 把 row 写入 board[col]
				place(col + 1)   // place(col 加 1)
			}
		}
	}
	place(0)       // place(0)
	return results // 返回 results
}

func main() { // 程序入口：跑内嵌自测用例
	sols := nQueensSafe() // 把 nQueensSafe() 写入 sols :
	ok := true            // 把 true 写入 ok :
	if len(sols) != 92 {  // 若 长度(sols) 不等于 92
		ok = false                                                   // 把 false 写入 ok
		fmt.Printf("FAIL nQueensSafe count=%d want 92\n", len(sols)) // 打印输出
	}
	if len(sols) >= 1 && fmt.Sprint(sols[0]) != "[1 5 8 6 3 7 2 4]" {
		ok = false                                                                // 把 false 写入 ok
		fmt.Printf("FAIL nQueensSafe first=%v want [1 5 8 6 3 7 2 4]\n", sols[0]) // 打印输出
	}
	if len(sols) >= 2 && fmt.Sprint(sols[len(sols)-1]) != "[8 4 1 3 6 2 7 5]" {
		ok = false                                                                         // 把 false 写入 ok
		fmt.Printf("FAIL nQueensSafe last=%v want [8 4 1 3 6 2 7 5]\n", sols[len(sols)-1]) // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
