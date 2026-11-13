// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145240191
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func exist(board [][]byte, word string) bool { // 定义函数/方法 exist
	if len(board) == 0 || len(board[0]) == 0 { // 若 长度(棋盘) 等于 0 或 长度(棋盘[0]) 等于 0
		return false // 返回 false
	}
	rows, cols := len(board), len(board[0]) // 把 长度(棋盘), 长度(棋盘[0]) 写入 rows, cols :
	var bt func(r, c, idx int) bool         // var bt func(右指针, 字符, idx int) bool
	bt = func(r, c, idx int) bool {         // 把 func(右指针, 字符, idx int) bool { 写入 bt
		if idx == len(word) { // 若 idx 等于 长度(单词
			return true // 返回 true
		}
		if r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != word[idx] {
			return false // 返回 false
		}
		ch := board[r][c] // 把 棋盘[右指针][字符] 写入 ch :
		board[r][c] = '#' // 把 '#' 写入 board[r][c]
		ok := bt(r+1, c, idx+1) || bt(r-1, c, idx+1) || bt(r, c+1, idx+1) || bt(r, c-1, idx+1)
		board[r][c] = ch // 把 字符 写入 board[r][c]
		return ok        // 返回 ok
	}
	for r := 0; r < rows; r++ { // 让 右指针 从 0 开始计数
		for c := 0; c < cols; c++ { // 让 字符 从 0 开始计数
			if bt(r, c, 0) { // 定义函数/方法 bt
				return true // 返回 true
			}
		}
	}
	return false // 返回 false
}

func main() { // 程序入口：跑内嵌自测用例
	b1 := [][]byte{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'}}
	cases := []struct { // 把 []struct { 写入 cases :
		board [][]byte // 棋盘 [][]byte
		word  string   // 单词 string
		want  bool     // want bool
	}{ // }{
		{b1, "ABCCED", true},
		{nil, "abc", false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := exist(c.board, c.word); g != c.want { // 若 g : 赋值为 exist(字符.棋盘, 字符.单词); g 不等于 字符.want
			ok = false                                                        // 把 false 写入 ok
			fmt.Printf("FAIL %v,%q=%v want %v\n", c.board, c.word, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
