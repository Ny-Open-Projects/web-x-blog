// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134032039
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

func eqMatrix(a, b [][]int) bool { // 定义函数/方法 eqMatrix
	if len(a) != len(b) {
		return false
	} // 若 长度(数组) 不等于 长度(b) { return false }
	for i := range a { // 把 range 数组 { 写入 for i :
		if len(a[i]) != len(b[i]) {
			return false
		} // 若 长度(数组[下标 i]) 不等于 长度(b[下标 i]) { return false }
		for j := range a[i] { // 把 range 数组[下标 i] { 写入 for j :
			if a[i][j] != b[i][j] {
				return false
			} // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j] { return false }
		}
	}
	return true // 返回 true
}

func rotate(matrix [][]int) { // 定义函数/方法 rotate
	n := len(matrix)         // 把 长度(矩阵) 写入 n :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		for j := i + 1; j < n; j++ { // 把 下标 i 加 1; 下标 j 小于 元素个数; 下标 j 加一 { 写入 for j :
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		for j, k := 0, n-1; j < k; j, k = j+1, k-1 {
			matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
		}
	}
}

func main() { // 程序入口：跑内嵌自测用例
	cases := [][2][][]int{ // 把 [][2][][]int{ 写入 cases :
		{{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}, {{7, 4, 1}, {8, 5, 2}, {9, 6, 3}}},
		{{{5, 1, 9, 11}, {2, 4, 8, 10}, {13, 3, 6, 7}, {15, 14, 12, 16}}, {{15, 13, 2, 5}, {14, 3, 4, 1}, {12, 6, 8, 9}, {16, 7, 10, 11}}},
	}
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		input := c[0]                   // 把 字符[0] 写入 input :
		expected := c[1]                // 把 字符[1] 写入 expected :
		rotate(input)                   // rotate(input)
		if !eqMatrix(input, expected) { // 若 取反 eqMatrix(input, expected
			fmt.Printf("FAIL: got %v expected %v\n", input, expected) // 打印输出
			os.Exit(1)                                                // os.Exit(1)
		}
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
