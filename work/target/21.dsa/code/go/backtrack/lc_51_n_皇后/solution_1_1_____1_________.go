// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239695
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func solveNQueens(n int) [][]string { // 定义函数/方法 solveNQueens
	solutions := [][]string{} // 把 [][]string{} 写入 solutions :
	queens := make([]int, n)  // 把 make([]int, 元素个数) 写入 queens :
	columns := map[int]bool{} // 把 映射表[int]bool{} 写入 columns :
	diag1 := map[int]bool{}   // 把 映射表[int]bool{} 写入 diag1 :
	diag2 := map[int]bool{}   // 把 映射表[int]bool{} 写入 diag2 :

	var generateBoard func() []string // var generateBoard func() []string
	generateBoard = func() []string { // 把 func() []string { 写入 generateBoard
		board := make([]string, n) // 把 make([]string, 元素个数) 写入 board :
		for i := 0; i < n; i++ {   // 让 下标 i 从 0 开始计数
			row := make([]byte, n) // 把 make([]byte, 元素个数) 写入 row :
			for j := range row {   // 把 range row { 写入 for j :
				row[j] = '.' // 把 '.' 写入 row[j]
			}
			row[queens[i]] = 'Q'   // 把 'Q' 写入 row[queens[i]]
			board[i] = string(row) // 把 string(row) 写入 board[i]
		}
		return board // 返回 棋盘
	}
	var backtrack func(row int) // var backtrack func(row int)
	backtrack = func(row int) { // 把 func(row int) { 写入 backtrack
		if row == n { // 若 row 等于 元素个数
			solutions = append(solutions, generateBoard()) // 把 append(solutions, generateBoard()) 写入 solutions
			return                                         // return
		}
		for col := 0; col < n; col++ { // 让 col 从 0 开始计数
			if columns[col] || diag1[row-col] || diag2[row+col] { // 若 columns[col] 或 diag1[row 减 col] 或 diag2[row 加 col]
				continue // 跳过本轮，进入下一次
			}
			queens[row] = col      // 把 col 写入 queens[row]
			columns[col] = true    // 把 true 写入 columns[col]
			diag1[row-col] = true  // 把 true 写入 diag1[row-col]
			diag2[row+col] = true  // 把 true 写入 diag2[row+col]
			backtrack(row + 1)     // backtrack(row 加 1)
			columns[col] = false   // 把 false 写入 columns[col]
			diag1[row-col] = false // 把 false 写入 diag1[row-col]
			diag2[row+col] = false // 把 false 写入 diag2[row+col]
		}
	}
	backtrack(0)     // backtrack(0)
	return solutions // 返回 solutions
}

func validNQueens(boards [][]string, n int) bool { // 定义函数/方法 validNQueens
	for _, b := range boards { // 同时取 _ 与 b 遍历
		if len(b) != n { // 若 长度(b) 不等于 元素个数
			return false // 返回 false
		}
		pos := [][2]int{}       // 把 [][2]int{} 写入 pos :
		for r, row := range b { // 同时取 右指针 与 row 遍历
			if len(row) != n { // 若 长度(row) 不等于 元素个数
				return false // 返回 false
			}
			for c, ch := range row { // 同时取 字符 与 字符 遍历
				if ch == 'Q' { // 若 字符 等于 'Q'
					pos = append(pos, [2]int{r, c}) // 把 append(pos, [2]int{右指针, 字符}) 写入 pos
				}
			}
		}
		if len(pos) != n { // 若 长度(pos) 不等于 元素个数
			return false // 返回 false
		}
		for i := 0; i < len(pos); i++ { // 让 下标 i 从 0 开始计数
			for j := i + 1; j < len(pos); j++ { // 把 下标 i 加 1; 下标 j 小于 长度(pos); 下标 j 加一 { 写入 for j :
				r1, c1 := pos[i][0], pos[i][1]                    // 把 pos[下标 i][0], pos[下标 i][1] 写入 r1, c1 :
				r2, c2 := pos[j][0], pos[j][1]                    // 把 pos[下标 j][0], pos[下标 j][1] 写入 r2, c2 :
				if c1 == c2 || r1-c1 == r2-c2 || r1+c1 == r2+c2 { // 若 c1 等于 c2 或 r1 减 c1 等于 r2 减 c2 或 r1 加 c1 等于 r2 加 c2
					return false // 返回 false
				}
			}
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true                         // 把 true 写入 ok :
	for _, n := range []int{4, 1, 2} { // 同时取 _ 与 元素个数 遍历
		boards := solveNQueens(n) // 把 solveNQueens(元素个数) 写入 boards :
		want := 0                 // 把 0 写入 want :
		switch n {                // switch 元素个数 {
		case 4: // case 4:
			want = 2 // 把 2 写入 want
		case 1: // case 1:
			want = 1 // 把 1 写入 want
		case 2: // case 2:
			want = 0 // 把 0 写入 want
		}
		if len(boards) != want { // 若 长度(boards) 不等于 want
			ok = false                                                                   // 把 false 写入 ok
			fmt.Printf("FAIL solveNQueens(%d) count=%d want %d\n", n, len(boards), want) // 打印输出
		}
		if !validNQueens(boards, n) { // 若 取反 validNQueens(boards, 元素个数
			ok = false                                             // 把 false 写入 ok
			fmt.Printf("FAIL solveNQueens(%d) invalid board\n", n) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
