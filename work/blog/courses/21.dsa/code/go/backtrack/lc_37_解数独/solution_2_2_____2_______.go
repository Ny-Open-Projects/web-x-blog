// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145238257
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
) // 引入依赖

func solveSudoku(board [9][9]string) [9][9]string { // 定义函数/方法 solveSudoku
	var valid func(r, c int, num string) bool // var valid func(右指针, 字符 int, num string) bool
	valid = func(r, c int, num string) bool { // 把 func(右指针, 字符 int, num string) bool { 写入 valid
		for i := 0; i < 9; i++ { // 让 下标 i 从 0 开始计数
			if board[i][c] == num { // 若 棋盘[下标 i][字符] 等于 num
				return false // 返回 false
			}
			if board[r][i] == num { // 若 棋盘[右指针][下标 i] 等于 num
				return false // 返回 false
			}
		}
		sr, sc := 3*(r/3), 3*(c/3) // 把 3 乘 (右指针 除以 3), 3 乘 (字符 除以 3) 写入 sr, sc :
		for i := 0; i < 3; i++ {   // 让 下标 i 从 0 开始计数
			for j := 0; j < 3; j++ { // 让 下标 j 从 0 开始计数
				if board[sr+i][sc+j] == num { // 若 棋盘[sr 加 下标 i][sc 加 下标 j] 等于 num
					return false // 返回 false
				}
			}
		}
		return true // 返回 true
	}
	digits := "123456789"     // 把 「123456789」 写入 digits :
	var backtrack func() bool // var backtrack func() bool
	backtrack = func() bool { // 把 func() bool { 写入 backtrack
		for r := 0; r < 9; r++ { // 让 右指针 从 0 开始计数
			for c := 0; c < 9; c++ { // 让 字符 从 0 开始计数
				if board[r][c] == "." { // 若 棋盘[右指针][字符] 等于 「.」
					for k := 0; k < 9; k++ { // 让 下标 k 从 0 开始计数
						num := string(digits[k]) // 把 string(digits[下标 k]) 写入 num :
						if valid(r, c, num) {    // 定义函数/方法 valid
							board[r][c] = num // 把 num 写入 board[r][c]
							if backtrack() {  // 定义函数/方法 backtrack
								return true // 返回 true
							}
							board[r][c] = "." // 把 「.」 写入 board[r][c]
						}
					}
					return false // 返回 false
				}
			}
		}
		return true // 返回 true
	}
	backtrack()  // backtrack()
	return board // 返回 棋盘
}

func main() { // 程序入口：跑内嵌自测用例
	board := [9][9]string{ // 把 [9][9]string{ 写入 board :
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
	got := solveSudoku(board) // 把 solveSudoku(棋盘) 写入 got :
	want := [9][9]string{     // 把 [9][9]string{ 写入 want :
		{"5", "3", "4", "6", "7", "8", "9", "1", "2"},
		{"6", "7", "2", "1", "9", "5", "3", "4", "8"},
		{"1", "9", "8", "3", "4", "2", "5", "6", "7"},
		{"8", "5", "9", "7", "6", "1", "4", "2", "3"},
		{"4", "2", "6", "8", "5", "3", "7", "9", "1"},
		{"7", "1", "3", "9", "2", "4", "8", "5", "6"},
		{"9", "6", "1", "5", "3", "7", "2", "8", "4"},
		{"2", "8", "7", "4", "1", "9", "6", "3", "5"},
		{"3", "4", "5", "2", "8", "6", "1", "7", "9"},
	}
	if !reflect.DeepEqual(got, want) { // 若 取反 reflect.DeepEqual(got, want
		fmt.Println("FAIL") // 打印输出
		os.Exit(1)          // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
