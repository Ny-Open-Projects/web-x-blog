// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240191
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func exist(board [][]byte, word string) bool { // 定义函数/方法 exist
	if len(board) == 0 || len(board[0]) == 0 { // 若 长度(棋盘) 等于 0 或 长度(棋盘[0]) 等于 0
		return false // 返回 false
	}
	m, n := len(board), len(board[0])                  // 把 长度(棋盘), 长度(棋盘[0]) 写入 m, n :
	var dfs func(r, c, idx int, visited [][]bool) bool // var dfs func(右指针, 字符, idx int, 已访问集合 [][]bool) bool
	dfs = func(r, c, idx int, visited [][]bool) bool { // 把 func(右指针, 字符, idx int, 已访问集合 [][]bool) bool { 写入 dfs
		if idx == len(word) { // 若 idx 等于 长度(单词
			return true // 返回 true
		}
		if r < 0 || r >= m || c < 0 || c >= n || visited[r][c] || board[r][c] != word[idx] {
			return false // 返回 false
		}
		visited[r][c] = true // 把 true 写入 visited[r][c]
		if dfs(r+1, c, idx+1, visited) || dfs(r-1, c, idx+1, visited) ||
			dfs(r, c+1, idx+1, visited) || dfs(r, c-1, idx+1, visited) {
			return true // 返回 true
		}
		visited[r][c] = false // 把 false 写入 visited[r][c]
		return false          // 返回 false
	}
	for i := 0; i < m; i++ { // 让 下标 i 从 0 开始计数
		for j := 0; j < n; j++ { // 让 下标 j 从 0 开始计数
			visited := make([][]bool, m) // 把 make([][]bool, 映射表) 写入 visited :
			for k := range visited {     // 把 range 已访问集合 { 写入 for k :
				visited[k] = make([]bool, n) // 把 make([]bool, 元素个数) 写入 visited[k]
			}
			if dfs(i, j, 0, visited) { // 定义函数/方法 dfs
				return true // 返回 true
			}
		}
	}
	return false // 返回 false
}

func main() { // 程序入口：跑内嵌自测用例
	board := [][]byte{ // 把 [][]byte{ 写入 board :
		{'A', 'B', 'C', 'E'},
		{'S', 'F', 'C', 'S'},
		{'A', 'D', 'E', 'E'},
	}
	ok := true                   // 把 true 写入 ok :
	if !exist(board, "ABCCED") { // 若 取反 exist(棋盘, 「ABCCED」
		ok = false                                     // 把 false 写入 ok
		fmt.Println("FAIL exist ABCCED expected true") // 打印输出
	}
	if !exist(board, "SEE") { // 若 取反 exist(棋盘, 「SEE」
		ok = false                                  // 把 false 写入 ok
		fmt.Println("FAIL exist SEE expected true") // 打印输出
	}
	if exist(board, "ABCB") { // 定义函数/方法 exist
		ok = false                                    // 把 false 写入 ok
		fmt.Println("FAIL exist ABCB expected false") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
