// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145239695
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func solveNQueens(n int) [][]string { // 定义函数/方法 solveNQueens
	res := [][]string{}                       // 把 [][]string{} 写入 res :
	cols := make([]bool, n)                   // 把 make([]bool, 元素个数) 写入 cols :
	diag1 := make([]bool, 2*n)                // 把 make([]bool, 2 乘 元素个数) 写入 diag1 :
	diag2 := make([]bool, 2*n)                // 把 make([]bool, 2 乘 元素个数) 写入 diag2 :
	var backtrack func(r int, board []string) // var backtrack func(右指针 int, 棋盘 []string)
	backtrack = func(r int, board []string) { // 把 func(右指针 int, 棋盘 []string) { 写入 backtrack
		if r == n { // 若 右指针 等于 元素个数
			cp := make([]string, len(board)) // 把 make([]string, 长度(棋盘)) 写入 cp :
			copy(cp, board)                  // copy(cp, 棋盘)
			res = append(res, cp)            // 把 append(结果, cp) 写入 结果
			return                           // return
		}
		for c := 0; c < n; c++ { // 让 字符 从 0 开始计数
			if cols[c] || diag1[r-c+n] || diag2[r+c] { // 若 列数[字符] 或 diag1[右指针 减 字符 加 元素个数] 或 diag2[右指针 加 字符]
				continue // 跳过本轮，进入下一次
			}
			cols[c] = true         // 把 true 写入 cols[c]
			diag1[r-c+n] = true    // 把 true 写入 diag1[r-c+n]
			diag2[r+c] = true      // 把 true 写入 diag2[r+c]
			row := make([]byte, n) // 把 make([]byte, 元素个数) 写入 row :
			for i := range row {   // 把 range row { 写入 for i :
				row[i] = '.' // 把 '.' 写入 row[i]
			}
			row[c] = 'Q'                               // 把 'Q' 写入 row[c]
			backtrack(r+1, append(board, string(row))) // backtrack(右指针 加 1, append(棋盘, string(row)))
			cols[c] = false                            // 把 false 写入 cols[c]
			diag1[r-c+n] = false                       // 把 false 写入 diag1[r-c+n]
			diag2[r+c] = false                         // 把 false 写入 diag2[r+c]
		}
	}
	backtrack(0, []string{}) // backtrack(0, []string{})
	return res               // 返回 结果
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
