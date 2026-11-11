// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238257
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func solveSudoku(board *[9][9]string) { // 定义函数/方法 solveSudoku
	var isValid func(row, col int, num string) bool // var isValid func(row, col int, num string) bool
	isValid = func(row, col int, num string) bool { // 把 func(row, col int, num string) bool { 写入 isValid
		for i := 0; i < 9; i++ { // 让 下标 i 从 0 开始计数
			if board[i][col] == num { // 若 棋盘[下标 i][col] 等于 num
				return false // 返回 false
			}
			if board[row][i] == num { // 若 棋盘[row][下标 i] 等于 num
				return false // 返回 false
			}
		}
		startRow, startCol := 3*(row/3), 3*(col/3) // 把 3 乘 (row 除以 3), 3 乘 (col 除以 3) 写入 startRow, startCol :
		for i := 0; i < 3; i++ {                   // 让 下标 i 从 0 开始计数
			for j := 0; j < 3; j++ { // 让 下标 j 从 0 开始计数
				if board[startRow+i][startCol+j] == num { // 若 棋盘[startRow 加 下标 i][startCol 加 下标 j] 等于 num
					return false // 返回 false
				}
			}
		}
		return true // 返回 true
	}
	var backtrack func() bool // var backtrack func() bool
	backtrack = func() bool { // 把 func() bool { 写入 backtrack
		for row := 0; row < 9; row++ { // 让 row 从 0 开始计数
			for col := 0; col < 9; col++ { // 让 col 从 0 开始计数
				if board[row][col] == "." { // 若 棋盘[row][col] 等于 「.」
					for num := '1'; num <= '9'; num++ { // 把 '1'; num 不超过 '9'; num 加一 { 写入 for num :
						s := string(num)          // 把 string(num) 写入 s :
						if isValid(row, col, s) { // 定义判定函数 isValid
							board[row][col] = s // 把 字符串 写入 board[row][col]
							if backtrack() {    // 定义函数/方法 backtrack
								return true // 返回 true
							}
							board[row][col] = "." // 把 「.」 写入 board[row][col]
						}
					}
					return false // 返回 false
				}
			}
		}
		return true // 返回 true
	}
	backtrack() // backtrack()
}

func validSudoku(b [9][9]string) bool { // 定义函数/方法 validSudoku
	for r := 0; r < 9; r++ { // 让 右指针 从 0 开始计数
		seen := map[string]bool{} // 把 映射表[string]bool{} 写入 seen :
		for c := 0; c < 9; c++ {  // 让 字符 从 0 开始计数
			v := b[r][c]             // 把 b[右指针][字符] 写入 v :
			if v == "." || seen[v] { // 若 值 等于 「.」 或 已见集合[值]
				return false // 返回 false
			}
			seen[v] = true // 把 true 写入 seen[v]
		}
	}
	for c := 0; c < 9; c++ { // 让 字符 从 0 开始计数
		seen := map[string]bool{} // 把 映射表[string]bool{} 写入 seen :
		for r := 0; r < 9; r++ {  // 让 右指针 从 0 开始计数
			v := b[r][c] // 把 b[右指针][字符] 写入 v :
			if seen[v] { // 若 已见集合[值]
				return false // 返回 false
			}
			seen[v] = true // 把 true 写入 seen[v]
		}
	}
	for br := 0; br < 3; br++ { // 让 br 从 0 开始计数
		for bc := 0; bc < 3; bc++ { // 让 bc 从 0 开始计数
			seen := map[string]bool{} // 把 映射表[string]bool{} 写入 seen :
			for i := 0; i < 3; i++ {  // 让 下标 i 从 0 开始计数
				for j := 0; j < 3; j++ { // 让 下标 j 从 0 开始计数
					v := b[br*3+i][bc*3+j] // 把 b[br 乘 3 加 下标 i][bc 乘 3 加 下标 j] 写入 v :
					if seen[v] {           // 若 已见集合[值]
						return false // 返回 false
					}
					seen[v] = true // 把 true 写入 seen[v]
				}
			}
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	original := [9][9]string{ // 把 [9][9]string{ 写入 original :
		{"5", "3", ".", ".", "7", ".", ".", ".", "."},
		{"6", ".", ".", "1", "9", "5", ".", ".", "."},
		{".", "9", "8", ".", ".", ".", ".", "6", "."},
		{"8", ".", ".", ".", "6", ".", ".", ".", "3"},
		{"4", ".", ".", "8", ".", "3", ".", ".", "1"},
		{"7", ".", ".", ".", "2", ".", ".", ".", "6"},
		{".", "6", ".", ".", ".", ".", "2", "8", "."},
		{".", ".", ".", "4", "1", "9", ".", ".", "5"},
		{".", ".", ".", ".", "8", ".", ".", "7", "9"},
	}
	board := original        // 把 original 写入 board :
	solveSudoku(&board)      // solveSudoku( 按位与 棋盘)
	ok := validSudoku(board) // 把 validSudoku(棋盘) 写入 ok :
	if ok {                  // 若 ok
		for r := 0; r < 9; r++ { // 让 右指针 从 0 开始计数
			for c := 0; c < 9; c++ { // 让 字符 从 0 开始计数
				if original[r][c] != "." && original[r][c] != board[r][c] {
					ok = false                                                                                      // 把 false 写入 ok
					fmt.Printf("FAIL original cell (%d,%d) changed: %s -> %s\n", r, c, original[r][c], board[r][c]) // 打印输出
				}
			}
		}
	} else { // 否则
		fmt.Println("FAIL solved board is not valid") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
